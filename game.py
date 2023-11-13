from player import Player
from property import Property
from board import Board
from square import Square
from collections import defaultdict
import random

class Game():
    """
    class enclosing the engine of the monopoly game
    """
    def __init__(self, players: list[Player], squares: list[Square], owners: dict[Property, Player]):
        self.players = players
        self.squares = squares
        self.owners = owners
        self.group_counts = defaultdict(int)
        for prop in owners.keys():
            self.group_counts[prop] += 1
        self.turns = 0
        self.doubles = 0
        self.rolled = 0
        self.taxes_to_pay = False
        self.card_to_draw = False
        self.rent_to_pay = False
        self.rent_owed = 0
        self.active_player = self.players[self.turns % len(self.players)]
    
    def active_square(self):
        """
        active_square returns the square that the active player is on
        """
        return self.squares[self.active_player.position]
    
    def active_property(self):
        """
        active_property returns the property belonging to the square the active player is on
        """
        return self.active_square().property

    def roll(self, dice=[6, 6]):
        """
        roll takes a list of integers representing the number of sides on the dice to roll,
        then returns a list of results for those dice being rolled
        """
        roll = []
        for i in dice:
            roll.append(random.randint(1, i))
        return roll

    def can_end_turn(self):
        """
        can_end_turn checks if the active player has any required actions left to take
        """
        return not (self.taxes_to_pay or self.card_to_draw or self.rent_to_pay) and self.rolled > 0
    
    def end_turn(self):
        """
        end_turn resets the turn based actions and increments the turn counter
        """
        self.turns += 1
        self.doubles = 0
        self.rolled = 0
        self.active_player = self.players[self.turns % len(self.players)]
    
    def calculate_rent(self, p: Property, dice_total = None):
        """Calculate the rent owed for a certain property, if unowned or mortgaged rent is 0"""
        owner = self.owners[p]
        if owner is None or p.mortgaged:
            return 0
        # If the property is a utility, rent depends on the dice rolled this turn
        if p.group == "Utility":
            if owner.get_group_counts(p.group) == 2:
                return p.rents[1] * dice_total
            else:
                return p.rents[0] * dice_total
        # If the property is a railroad, rent just depends on how many railroads the owner owns
        elif p.group == "Railroad":
            return p.rents[0] * owner.get_group_counts(p.group)
        # Otherwise, rent depends on whether the player has a monopoly and the buildings on the property
        else:
            monopoly = owner.get_group_counts(p.group) == self.group_counts(p.group)
            if monopoly and p.building_count == 0:
                return p.rents[0] * 2
            elif monopoly:
                return p.rents[p.building_count]
            else:
                return p.rents[0]
    
    def buy_property(self, property: Property, player: Player, price = None):
        """
        Handle the buying and selling of property, at base or any other price
        If purchase goes through, returns True
        If player cannot afford the property, returns False
        """
        if price is None:
            price = property.price
        if player.money < price:
            return False
        if self.owners[property] is not None:
            self.owners[property].money += price
        player.money -= price
        self.owners[property] = player
        player.properties.append(property)
        return True
    
    def move_player(self, player: Player, squares: int):
        """
        Move a player a given number of squares
        Check if they pass go, if so they gain 200 money
        """
        player.money += 200 * ((player.position + squares) // len(self.squares))
        player.position = (player.position + squares) % len(self.squares)
    
    def roll_move(self):
        """
        roll dice and move a player, updating rolls and doubles. Send player to jail at 3 doubles
        """
        roll = self.roll()
        self.rolled += 1
        if roll[0] == roll[1]:
            self.doubles += 1
        if self.doubles >= 3:
            self.send_to_jail(self.active_player)
        else:
            self.move_player(self.active_player, roll[0]+roll[1])
            self.add_actions(roll)
    
    def send_to_jail(self, player:Player):
        """
        send_to_jail sends a given player to jail, setting their position and jailtime
        accordingly
        """
        player.position = 10
        player.jailtime = 1

    def add_actions(self, dice: list[int]):
        """
        add_actions updates the appropriate flags based on which square a player landed on
        """
        if self.active_player.jailtime > 0:
            # Actions if the player is in jail
            pass
        else:
            # Actions if the player is not in jail
            if self.active_property().group == "Tax":
                self.taxes_to_pay = True
            elif self.active_property().group in ["Chance", "Chest"]:
                self.card_to_draw = True
            elif self.active_property().group not in ["Go", "Jail", "Parking", "GoToJail"]:
                if self.owners(self.active_property()) != self.active_player:
                    self.rent_owed = self.calculate_rent(self.active_property(), sum(dice))
                    if self.rent_owed > 0:
                        self.rent_to_pay = True
    
    def pay_rent(self):
        """
        pay_rent removes money from the active player equal to the rent owed,
        and adds it to the player owning the property they are on
        """
        self.active_player.money -= self.rent_owed
        self.owners[self.active_property()].money += self.rent_owed
        self.rent_owed = 0
        self.rent_to_pay = False

    def legal_actions(self):
        """
        legal_actions returns a list of actions that the active player can take
        actions are: roll_move, roll_jail, pay_fine, pay_rent, draw_card, pay_tax, end_turn
        """
        actions = []
        if self.active_player.jailtime > 0:
            # Active player is in jail
            if self.rolled == 0:
                # If they haven't rolled yet, they can either roll or pay the fine
                actions += ["roll_jail", "pay_fine"]
            else:
                actions += ["end_turn"]
        else:
            # Active player is not in jail
            if self.rent_to_pay:
                actions += ["pay_rent"]
            elif self.card_to_draw:
                actions += ["draw_card"]
            elif self.taxes_to_pay:
                actions += ["pay_tax"]
            else:
                if self.rolled <= self.doubles:
                    actions += ["roll_move"]
                else:
                    actions += ["end_turn"]
        