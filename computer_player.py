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
            if "roll_move" in game.legal_actions()[0]:
                pass
            elif "roll_jail" in game.legal_actions()[0]:
                pass
    
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