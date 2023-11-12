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