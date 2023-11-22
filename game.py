from player import Player
from property import Property
from board import Board
from square import Square
from deck import Deck
from collections import defaultdict
import random
import arcade

DEBUG = False

class Game():
    """
    class enclosing the engine of the monopoly game
    """
    def __init__(self, players: list, squares: list, owners: dict, card_scale: int):
        self.players = players
        self.squares = squares
        self.owners = owners
        self.group_counts = defaultdict(int)
        for prop in owners.keys():
            self.group_counts[prop.group] += 1
        # Track how many houses/hotels the bank has left
        self.bank_houses = 32
        self.bank_hotels = 12
        self.turns = 0
        self.doubles = 0
        self.rolled = 0
        self.taxes_to_pay = False
        self.card_to_draw = False
        self.rent_to_pay = False
        self.rent_owed = 0
        self.active_player = self.players[self.turns % len(self.players)]
        self.chance = Deck("Chance", [], card_scale)
        self.chest = Deck("Community Chest", [], card_scale)
        self.card = None
        self.SCREEN_WIDTH = card_scale

        self.die_sprites = arcade.SpriteList()
    
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
    
    def square_action(self, square: Square):
        if square.property.group == "Tax":
            return "pay_tax"
        elif square.property.group in ["Chance", "Chest"]:
            return "draw_card"
        elif square.property.group not in ["Go", "Jail", "Parking", "GoToJail"]:
            return "property_action"
        else:
            return "no_action"

    def roll(self, dice=[6, 6]):
        """
        roll takes a list of integers representing the number of sides on the dice to roll,
        then returns a list of results for those dice being rolled
        """
        # Debugging console entry for dice values
        if DEBUG:
            s = input("Enter the dice rolls as i, i: ")
            return [int(v) for v in s.split(",")]
        roll = []
        for i in dice:
            roll.append(random.randint(1, i))

        # DICE RENDER FUNCTIONALITY
        self.die_sprites.clear()
        die_list = []
        i = 0
        while i < 2:
            tile_width = ((self.SCREEN_WIDTH-200)*(3/4))/9
            scaling = (tile_width/1.5)/350
            png_name = "assets/die" + str(roll[i]) + ".png"
            die_sprite = arcade.Sprite(png_name, scaling)
            rand_x = random.randint((tile_width*3)*(-1), tile_width*3)
            rand_y = random.randint((tile_width*3)*(-1), tile_width*3)
            die_sprite.center_x = self.SCREEN_WIDTH/2 + rand_x
            die_sprite.center_y = self.SCREEN_WIDTH/2 + rand_y
            die_sprite.angle = random.randint(0, 90)
            die_list.append(die_sprite)
            # Check for overlapping dice and restart if so
            if (i == 1) and (arcade.check_for_collision(die_list[0], die_list[1])):
                die_list.clear()
                i = 0
            else:
                i += 1
        for s in die_list:
            self.die_sprites.append(s)

        return roll

    def can_end_turn(self):
        """
        can_end_turn checks if the active player has any required actions left to take
        """
        return not (self.taxes_to_pay or self.card_to_draw or self.rent_to_pay) and self.rolled > 0
    
    def end_turn(self):
        """
        end_turn resets the turn based actions and increments the turn counter
        If the player tries to end their turn with a balance less than 0, the game ends and
        their properites are returned to the bank
        """
        if self.active_player.money < 0:
            # Remove properties from player
            self.active_player.properties = []
            
            # Return player's properties to the bank
            for p in self.owners:
                if self.owners[p] == self.active_player:
                    self.owners[p] = None

            # Game is over
            return -1
        else:
            if self.active_player.jailtime > 0:
                # If they player is in jail, increment how long they have been there
                self.active_player.jailtime += 1
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
            if owner.get_group_counts()[p.group] == 2:
                return p.rents[1] * dice_total
            else:
                return p.rents[0] * dice_total
        # If the property is a railroad, rent just depends on how many railroads the owner owns
        elif p.group == "Railroad":
            return p.rents[0] * owner.get_group_counts()[p.group]
        # Otherwise, rent depends on whether the player has a monopoly and the buildings on the property
        else:
            monopoly = owner.get_group_counts()[p.group] == self.group_counts[p.group]
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
        if property.group != "Parking" and self.owners[property] is not None:
            self.owners[property].money += price
        player.money -= price
        self.owners[property] = player
        player.properties.append(property)
        return True
    
    def can_buy_house(self, property: Property, player: Player):
        """
        can_buy_house checks if the given player can buy a house on the given property
        returns True if they can, False if not
        """
        # Make sure the player has a monopoly
        monopoly = self.group_counts[property.group] == player.get_group_counts()[property.group]
        # Make sure the property isn't mortgaged
        if monopoly and not property.mortgaged:
            # Check the minimum number of houses on each property in the group
            min_building_count = 5
            for prop in self.owners.keys():
                if prop.group == property.group and prop.building_count < min_building_count:
                    min_building_count = prop.building_count
            # If the property does not have a hotel, and is among the least developed properties in the group,
            # and the bank has a house or hotel, return True
            if property.building_count < 5 and property.building_count == min_building_count:
                if property.building_count < 4:
                    return self.bank_houses > 0
                elif property.building_count == 4:
                    return self.bank_hotels > 0
        # Otherwise, return False
        return False
    
    def can_sell_house(self, property: Property):
        """
        can_sell_house checks if the given player can sell a house on the given property
        returns True if they can, False if not
        """
        max_building_count = 0
        for prop in self.owners.keys():
            if prop.group == property.group and prop.building_count > max_building_count:
                max_building_count = prop.building_count
        return (property.building_count == max_building_count and property.building_count > 0)
    
    def buy_house(self, property: Property, player: Player):
        """
        buy_house has the given player buy a house on the given property
        returns True if successful, False if not
        """
        # If the player cannot buy a house/hotel on the property, return False
        if not self.can_buy_house(property, player) or player.money < property.building_cost:
            return False
        # Otherwise, update the information around buying the house/hotel and return True
        if property.building_count == 4:
            self.bank_houses += 4
            self.bank_hotels -= 1
        else:
            self.bank_houses -= 1
        property.building_count += 1
        player.money -= property.building_cost
        return True
    
    def sell_house(self, property: Property, player: Player):
        """
        sell_house has the given player sell a hosue on the given property
        returns True if successful, False if not
        """
        if not self.can_sell_house(property):
            return False
        if property.building_count == 5:
            self.bank_houses -= 4
            self.bank_hotels += 1
        else:
            self.bank_houses += 1
        property.building_count -= 1
        player.money += property.building_cost // 2
        return True
    
    def can_mortgage(self, property: Property):
        """
        can_mortgage returns true if the given property can be mortgaged
        """
        return property.building_count == 0 and not property.mortgaged
    
    def can_unmortgage(self, property: Property, player: Player):
        """
        can_unmortgage returns true if the given property can be unmortgaged by the given player
        """
        if self.owners[property] is not player or not property.mortgaged:
            return False
        return player.money >= property.mortgage_value * 1.1
    
    def mortgage(self, property: Property, player: Player):
        """
        mortgage has the given player mortgage the given property
        returns True if successful, False if not
        """
        if self.owners[property] is not player or property.mortgaged or not self.can_mortgage(property):
            return False
        player.money += property.mortgage_value
        property.mortgaged = True
        return True
    
    def unmortgage(self, property: Property, player: Player):
        """
        unmortgage has the given player unmortgage the given property
        returns True if successful, False if not
        """
        if not self.can_unmortgage(property, player):
            return False
        player.money -= int(property.mortgage_value * 1.1)
        property.mortgaged = False
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
            # If move lands player on Go to Jail, send the player to jail
            if self.active_player.position == 30:
                self.send_to_jail(self.active_player)
        
        return roll
    
    def roll_jail(self):
        """
        roll_jail handles the player rolling dice to get out of jail
        """
        roll = self.roll()
        self.rolled += 1
        if roll[0] == roll[1]:
            # If the player rolls doubles, they get out of jail and move that far
            self.active_player.jailtime = 0
            self.move_player(self.active_player, sum(roll))
            self.add_actions(roll)
        elif self.active_player.jailtime > 3:
            # If the player has been in jail for 3 turns and doesn't roll doubles, they must pay the fine and move the amount they rolled
            self.pay_fine()
            self.move_player(self.active_player, sum(roll))
            self.add_actions(roll)
    
    def pay_fine(self):
        """
        pay_fine handles a player paying their fine from jail
        """
        self.active_player.money -= 50
        self.active_player.jailtime = 0
    
    def card_jail(self):
        """
        card_jail handles a player using their get out of jail free card
        returns False if the player did not have a card, True otherwise
        """
        if self.active_player.jail_free == []:
            return False
        self.active_player.jailtime = 0
        if self.active_player.jail_free[0].card_type == "Chance":
            self.chance.cards.append(self.active_player.jail_free[0])
        elif self.active_player.jail_free[0].card_type == "Community Chest":
            self.chest.cards.append(self.active_player.jail_free[0])
        del self.active_player.jail_free[0]
        return True
    
    def send_to_jail(self, player:Player):
        """
        send_to_jail sends a given player to jail, setting their position and jailtime
        accordingly
        """
        player.position = 10
        player.jailtime = 1

    def add_actions(self, dice: list):
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
                if self.owners[self.active_property()] != self.active_player:
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
    
    def pay_tax(self):
        """
        pay_tax removes money from the active player equal to the amount of tax
        owed, based on which tax square they are on
        """
        if self.active_property().name == "Income Tax":
            self.active_player.money -= 200
        elif self.active_property().name == "Luxury Tax":
            self.active_player.money -= 100
        self.taxes_to_pay = False
    
    def draw_card(self):
        """
        draw_card draws a card from the appropriate deck and performs the card's
        action on the player
        """
        # Draw the card
        if self.active_property().name == "Chance":
            card = self.chance.draw_card()
        else:
            card = self.chest.draw_card()
        self.card = card

        # Implement card's effect on the player
        effect = card.return_effect(self.active_player.position, self.active_player)
        if effect[0] == "money":
            self.active_player.money += effect[1]
        elif effect[0] == "money_players":
            self.active_player.money += (len(self.players) - 1) * effect[1]
            for player in range(len(self.players)):
                if self.players[player].player_no != self.active_player.player_no:
                    self.players[player].money += -effect[1]
        elif effect[0] == "money_houses":
            for property in self.active_player.properties:
                if property.building_count == 5:
                    self.active_player.money += 4 * effect[1]
                    self.active_player.money += effect[2]
                else:
                    self.active_player.money += property.building_count * effect[1]
        elif effect[0] == "move_jail":
            self.send_to_jail(self.active_player)
        elif effect[0] == "move" or effect[0] == "move_utility" or effect[0] == "move_rr" or effect[0] == "move_abs":
            self.active_player.position = effect[1]
        else:
            self.active_player.jail_free.append(card)
        
        self.card_to_draw = False

    def legal_actions(self):
        """
        legal_actions returns a list of actions that the active player can take
        actions are: roll_move, roll_jail, rolled_jail, pay_fine, pay_rent, draw_card, pay_tax, end_turn, buy_property, own_property, card_jail
        """
        required_actions = []
        other_actions = []
        stubs = []
        if self.active_player.jailtime > 0:
            # Active player is in jail
            if self.rolled == 0:
                # If they haven't rolled yet, they can either roll or pay the fine
                required_actions += ["roll_jail", "pay_fine"]
                if self.active_player.jail_free != []:
                    other_actions += ["card_jail"]
            else:
                required_actions += ["end_turn", "rolled_jail"]
        else:
            # Active player is not in jail
            if self.rolled <= self.doubles:
                roll_end = "roll_move"
            else:
                roll_end = "end_turn"
            if self.rent_to_pay:
                required_actions += ["pay_rent"]
            elif self.card_to_draw:
                required_actions += ["draw_card"]
            elif self.taxes_to_pay:
                required_actions += ["pay_tax"]
            elif self.square_action(self.active_square()) != "property_action":
                if self.rolled > 0:
                    stubs += [self.square_action(self.active_square())]
            else:
                if self.owners[self.active_property()] == self.active_player:
                    stubs += ["own_property"]
                elif self.rolled > 0 and self.owners[self.active_property()] is None:
                    other_actions += ["buy_property"]
                elif self.rolled > 0:
                    stubs += ["pay_rent"]
            if len(required_actions) > 0:
                stubs += [roll_end]
            else:
                required_actions += [roll_end]
        
        return required_actions, other_actions, stubs
            

