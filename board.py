import arcade
from square import Square
from property import Property
from player import Player
from collections import defaultdict
import csv

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Monopoly!"


class Board(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        #initialize squares list
        self.squares = []
        # List of all properties kept for accessibility
        self.properties = []
        # Initialize dictionary to track property ownership
        self.owners = {}
        # Initialize a defaultdict(int) to count property types
        self.group_counts = defaultdict(int)
        with open("board.csv") as board_file:
            boardreader = csv.DictReader(board_file)
            for line in boardreader:
                p = None
                # Create the property from the CSV file (the None values are for mortgage and building cost, which aren't in the CSV yet)
                if line['Space'] == 'Street':
                    p = Property(line['Name'], line['Color'], int(line['Price']), [int(line['Rent'])] + [int(line[f'RentBuild{i}']) for i in range(1, 6)], None, None)
                elif line['Space'] == 'Railroad' or line['Space'] == 'Utility':
                    p = Property(line['Name'], line['Space'], int(line['Price']), [int(line['Rent'])], None, None)
                if p is not None:
                    # Add the property to the list of properties
                    self.properties.append(p)
                    self.owners[p] = None
                    self.group_counts[p.group] += 1
                # Add the square to the list of squares, was unsure what to initialize x/y/height/width to
                self.squares.append(Square(line['Name'], p, 0, 0, 0, 0))
        
        self.players = []
        self.turn = 0

    def on_draw(self):
        self.clear()
        logo = arcade.load_texture("assets/logo.png")
        logo_scale = .4
        logo_tilt_angle = -45
        board_color = arcade.color.BLACK
        board_center_x = 300
        board_center_y = 300
        inner_board_width = 300
        inner_board_height = 300
        outer_board_width = 400
        outer_board_height = 400
        border_width = 1
        tile_width = 33.3333
        tile_height = 50
        num_tiles = round(inner_board_width / tile_width)
        row_tile_x = 166
        bottom_tile_y = 125
        top_tile_y = 475
        column_tile_y = 167
        left_tile_x = 125
        right_tile_x = 475
        bottom_tile_tilt = 0
        right_tile_tilt = 90
        top_tile_tilt = 180
        left_tile_tilt = 270
        left_corners_x = 125
        bottom_corners_y = 125
        right_corners_x = 475
        top_corners_y = 475
        corner_tile_width = 50
        corner_tile_height = 50


        #draw logo
        arcade.draw_scaled_texture_rectangle(self.width/2, self.height/2, logo, logo_scale, logo_tilt_angle)

        #draw inner square of board
        arcade.draw_rectangle_outline(board_center_x, board_center_y, inner_board_width,
                                      inner_board_height, board_color, border_width)

        #draw outer square of board
        arcade.draw_rectangle_outline(board_center_x, board_center_y, outer_board_width,
                                      outer_board_height, board_color, border_width)

        property = Property("test", 0, [], 0, 0)


        #call square for each tile in bottom row
        for i in range(0, num_tiles):

            square = Square("test", property, row_tile_x, bottom_tile_y, tile_width, tile_height)
            square.draw(row_tile_x, bottom_tile_y, bottom_tile_tilt)

            row_tile_x += tile_width

        #reset x value for top row
        row_tile_x = 166

        #call square for each tile in top row
        for i in range(0, num_tiles):
            square = Square("test", property, row_tile_x, top_tile_y, tile_width, tile_height)
            square.draw(row_tile_x, top_tile_y, top_tile_tilt)

            row_tile_x += tile_width

        #call square for each tile in right column
        for i in range(0, num_tiles):
            square = Square("test", property, right_tile_x, column_tile_y, tile_width, tile_height)
            square.draw(right_tile_x, column_tile_y, right_tile_tilt)

            column_tile_y += tile_width

        #reset y value for left column
        column_tile_y = 167

        #call square for each tile in left column
        for i in range(0, num_tiles):
            square = Square("test", property, left_tile_x, column_tile_y, tile_width, tile_height)
            square.draw(left_tile_x, column_tile_y, left_tile_tilt)

            column_tile_y += tile_width

        #call corner tile special cases
        square = Square("test", property, left_corners_x, bottom_corners_y, corner_tile_width, corner_tile_height)
        square.draw(left_corners_x, bottom_corners_y, bottom_tile_tilt)
        square = Square("test", property, left_corners_x, top_corners_y, corner_tile_width, corner_tile_height)
        square.draw(left_corners_x, top_corners_y, bottom_tile_tilt)
        square = Square("test", property, right_corners_x, bottom_corners_y, corner_tile_width, corner_tile_height)
        square.draw(right_corners_x, bottom_corners_y, bottom_tile_tilt)
        square = Square("test", property, right_corners_x, top_corners_y, corner_tile_width, corner_tile_height)
        square.draw(right_corners_x, top_corners_y, bottom_tile_tilt)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
    
    """Game Logic Functions"""
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
        return True

    def move_player(self, player: Player, squares: int):
        """
        Move a player a given number of squares
        Check if they pass go, if so they gain 200 money
        """
        player.money += 200 * ((player.position + squares) // len(self.squares))
        player.position = (player.position + squares) % len(self.squares)
    
    def roll():
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        rolls = (roll1, roll2)
        return rolls


def main():
    """ Main function """
    game = Board(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
