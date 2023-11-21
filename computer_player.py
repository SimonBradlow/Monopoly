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
        super.__init__(pNumber, piece, scale, position, properties, money, jailtime, jail_free)
    
    def take_turn(self, game: Game):
        """
        take_turn checks if this object is the active player, and if so takes their turn in the given game
        """
        # Check that this ComputerPlayer is the active player
        if not game.active_player is self:
            return False
        
        # Loop until turn is complete
        done = False

        while not done:
            required_actions, other_actions, stubs = game.legal_actions()
            if "roll_move" in required_actions:
                game.roll_move()
            elif "roll_jail" in required_actions:
                if self.should_pay_fine():
                    game.pay_fine()
                else:
                    game.roll_jail()
            if "pay_rent" in required_actions:
                game.pay_rent()
            elif "draw_card" in required_actions:
                game.draw_card()
            elif "pay_tax" in required_actions:
                game.pay_tax()
            if "buy_property" in other_actions:
                if self.should_buy(game.active_property, game):
                    game.buy_property(game.active_property, self)
            self.buy_upgrades(game)
            if "end_turn" in game.legal_actions()[0]:
                done = True
                game.end_turn()
        return True
    
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