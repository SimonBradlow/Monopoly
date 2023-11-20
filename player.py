import arcade
from collections import defaultdict
from typing import List
from property import Property

PIECE_LIST = ["car", "dog", "hat", "ship", "boot", "iron", "thimble", "wheelbarrow"]

class Player():
    """
    class representing individual player in monopoly
    """
    def __init__(self, pNumber, piece, scale, position: int =0, properties: list =[], money: int =1500, jailtime: int = 0, jail_free = False):
        self.player_no = pNumber
        self.position = position
        self.properties = properties
        self.money = money
        self.jailtime = jailtime
        self.jail_free = jail_free

        self.piece = piece
        self.sprite_list = arcade.SpriteList()
        
        self.scale = scale
        scaling = (scale/2)/400
        png_name = "assets/" + PIECE_LIST[self.piece] + ".png"
        player_sprite = arcade.Sprite(png_name, scaling)
        player_sprite.center_x = 0
        player_sprite.center_y = 0
        self.sprite_list.append(player_sprite)


    def get_group_counts(self):
        # Count how many of each type of property the player owns, return it as a defaultdict(int)
        counts = defaultdict(int)
        for p in self.properties:
            counts[p.group] += 1
        return counts

    def draw(self, x, y):
        for s in self.sprite_list:
            s.center_x = x + ((self.scale/4)*((-1)**self.player_no))
            s.center_y = y + ((self.scale/4)*((-1)**(self.player_no//2)))
        self.sprite_list.draw()
