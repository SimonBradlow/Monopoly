import arcade
from square import Square
from property import Property
from gameOverView import GameOverView
import csv

class Board(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.width = 600
        self.height = 600
        arcade.set_background_color(arcade.color.AMAZON)


        # If you have sprite lists, you should create them here,
        # and set them to None

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        #initialize squares list
        self.squares = []
        with open('board.csv', mode ='r') as board_file:
            boardreader = csv.DictReader(board_file)
            for line in boardreader:
                width = 33.3333
                height = 50
                p = None
                # Create the property from the CSV file (the None values are for mortgage and building cost, which aren't in the CSV yet)
                corner_names = ['Go', 'Jail', 'Parking', 'GoToJail']
                non_property_names = ['Railroad', 'Utility', 'Tax', 'Chance', 'Chest']
                if line['Space'] == 'Street':
                    p = Property(line['Name'], line['Color'], int(line['Price']), [int(line['Rent'])] + [int(line[f'RentBuild{i}']) for i in range(1, 6)], None, None)
                elif line['Space'] in non_property_names:
                    p = Property(line['Name'], line['Space'], int(line['Price']), [int(line['Rent'])], None, None)
                elif line['Space'] in corner_names:
                    p = Property(line['Name'], line['Space'], int(line['Price']), [int(line['Rent'])], None, None)
                    width = 50
                # Add the square to the list of squares, was unsure what to initialize x/y/height/width to
                self.squares.append(Square(int(line['Position']), p, width, height))

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
        corner_tile_tilt = -90

        #draw logo
        arcade.draw_scaled_texture_rectangle(self.width/2, self.height/2, logo, logo_scale, logo_tilt_angle)

        #draw inner square of board
        arcade.draw_rectangle_outline(board_center_x, board_center_y, inner_board_width,
                                      inner_board_height, board_color, border_width)

        #draw outer square of board
        arcade.draw_rectangle_outline(board_center_x, board_center_y, outer_board_width,
                                      outer_board_height, board_color, border_width)

        #draw community chest
        arcade.draw_rectangle_outline(225, 225, 40,
                                      80, board_color, border_width, logo_tilt_angle - 90)

        #draw chance
        arcade.draw_rectangle_outline(375, 375, 40,
                                      80, board_color, border_width, logo_tilt_angle - 90)

        property = Property("test", "test", 0, [], 0, 0)

        #draw go tile at position 0
        self.squares[0].draw(left_corners_x, bottom_corners_y, corner_tile_tilt)

        # call square for each tile in left column
        for i in range(1, num_tiles + 1):
            self.squares[i].draw(left_tile_x, column_tile_y, left_tile_tilt)

            column_tile_y += tile_width

        #draw jail tile at position 10
        self.squares[10].draw(left_corners_x, top_corners_y, corner_tile_tilt)

        # call square for each tile in top row
        for i in range(11, num_tiles + 11):
            self.squares[i].draw(row_tile_x, top_tile_y, top_tile_tilt)

            row_tile_x += tile_width

        #draw free parking tile at position 20
        self.squares[20].draw(right_corners_x, top_corners_y, corner_tile_tilt)

        #reset column y
        column_tile_y = 433

        # call square for each tile in right column
        for i in range(21, num_tiles + 21):
            self.squares[i].draw(right_tile_x, column_tile_y, right_tile_tilt)

            column_tile_y -= tile_width

        #draw go to jail at position 30
        self.squares[30].draw(right_corners_x, bottom_corners_y, corner_tile_tilt)

        #reset row x
        row_tile_x = 433

        #call square for each tile in bottom row
        for i in range(31, num_tiles + 31):

            self.squares[i].draw(row_tile_x, bottom_tile_y, bottom_tile_tilt)

            row_tile_x -= tile_width





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

        if key == 65307:
            board_view = GameOverView()
            self.window.show_view(board_view)

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
