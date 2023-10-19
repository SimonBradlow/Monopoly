from collections import defaultdict
from property import Property

class Player():
    """
    class representing individual player in monopoly
    """
    def __init__(self, position: int =0, properties: list[Property] =[], money: int =1500, jailtime: int = 0):
        self.position = position
        self.properties = properties
        self.money = money
        self.jailtime = jailtime

    def get_group_counts(self):
        # Count how many of each type of property the player owns, return it as a defaultdict(int)
        counts = defaultdict(int)
        for p in self.properties:
            counts[p.group] += 1
        return counts

    def draw():
        pass