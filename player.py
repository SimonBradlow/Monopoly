import arcade

PIECE_LIST = ["car", "dog", "hat", "ship"]

class Player():
    """
    class representing individual player in monopoly
    """
    def __init__(self, player, piece, scale):
        self.player_no = player
        self.board_pos = 0

        self.piece = piece
        self.sprite_list = arcade.SpriteList()
        
        self.scale = scale
        scaling = (scale/2)/400
        png_name = "assets/" + PIECE_LIST[self.piece] + ".png"
        player_sprite = arcade.Sprite(png_name, scaling)
        player_sprite.center_x = 0
        player_sprite.center_y = 0
        self.sprite_list.append(player_sprite)

    def draw(self, x, y):
        for s in self.sprite_list:
            s.center_x = x + ((self.scale/4)*((-1)**self.player_no))
            s.center_y = y + ((self.scale/4)*((-1)**(self.player_no//2)))
        self.sprite_list.draw()
