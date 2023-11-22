from player import Player
from game import Game
from property import Property
import random

class ComputerPlayer(Player):
    """
    ComputerPlayer class is a Player that can also make its own moves in a Game object
    """
    def __init__(self, pNumber, piece, scale, position: int=0, properties: list =[], money: int =1500, jailtime: int = 0, jail_free = False):
        """
        ComputerPlayer initializer calls Player intializer
        """
        super().__init__(pNumber, piece, scale, position, properties, money, jailtime, jail_free)
        self.log = []
    
    def take_turn(self, game: Game):
        """
        take_turn checks if this object is the active player, and if so takes their turn in the given game
        returns a boolean if the player took a turn, and a list of string actions they took during their turn
        """
        # Check that this ComputerPlayer is the active player
        if not game.active_player is self:
            return False, []
        
        # Loop until turn is complete
        done = False
        self.log = []
        while not done:
            required_actions, other_actions, stubs = game.legal_actions()
            if "roll_move" in required_actions:
                roll = game.roll_move()
                self.log.append(f"Computer rolled {roll}, moving to {game.active_property().name}")
            elif "roll_jail" in required_actions:
                if "card_jail" in other_actions and self.should_use_jail_free(game):
                    game.card_jail()
                    self.log.append(f"Computer used Get Out of Jail Free!")
                elif self.should_pay_fine(game):
                    game.pay_fine()
                    self.log.append(f"Computer paid $50 fine to get out of jail")
                else:
                    game.roll_jail()
                    self.log.append(f"Computer rolled to get out of jail")
            if "pay_rent" in required_actions:
                self.log.append(f"Computer paid ${game.rent_owed} to owner of {game.active_property().name}")
                game.pay_rent()
            elif "draw_card" in required_actions:
                self.log.append("Computer drew a card")
                game.draw_card()
            elif "pay_tax" in required_actions:
                self.log.append("Computer paid their taxes")
                game.pay_tax()
            if "buy_property" in other_actions:
                if self.should_buy(game.active_property(), game):
                    self.log.append(f"Computer bought {game.active_property().name} for {game.active_property().price}")
                    game.buy_property(game.active_property(), self)
            if "end_turn" in required_actions:
                self.buy_upgrades(game)
                self.log.append(f"Computer ended their turn")
                done = True
                game.end_turn()
        return True, self.log
    
    def buy_upgrades(self, game: Game):
        """
        buy_upgrades goes through all the properties this ComputerPlayer owns, buying upgrades until
        should_upgrade tells it not to
        """
        bought = True

        while bought:
            bought = False
            for prop in self.properties:
                if self.should_upgrade(prop, game):
                    game.buy_house(prop, self)
                    bought = True
    
    def should_buy(self, property: Property, game: Game):
        """
        should_buy returns true if the ComputerPlayer will buy the given property in the given game,
        False if it will not
        """
        if self.money < property.price:
            return False
        return random.random() > 0.5

    def should_upgrade(self, property: Property, game: Game):
        """
        should_upgrade returns true if the ComputerPlayer will upgrade the given property in the given
        game, False if it will not
        """
        if not game.can_buy_house(property, self) or self.money < property.building_cost:
            return False
        return property.building_count < 4
    
    def should_pay_fine(self, game: Game):
        """
        should_pay_fine determines if the ComputerPlayer should pay their fine to get out of jail
        """
        if self.money < 50:
            return False
        return random.random() > 0.5

    def should_use_jail_free(self, game: Game):
        """
        should_use_jail_free determines if the ComputerPlayer should use their get out of jail free card
        """
        if not self.jail_free:
            return False
        return random.random() > 0.5