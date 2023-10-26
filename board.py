import arcade
from square import Square
from property import Property
import csv

class Board():
    def __init__(self, w, h, e):
        # Initialize squares list
        self.squares = []
        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e
        with open('board.csv', mode ='r') as board_file:
            boardreader = csv.DictReader(board_file)
            for line in boardreader:
                width = ((self.SCREEN_WIDTH-(self.EDGE_SPACE*2))*(3/4))/9
                height = (self.SCREEN_HEIGHT-(self.EDGE_SPACE*2))/8
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
                    width = height
                # Add the square to the list of squares, was unsure what to initialize x/y/height/width to
                self.squares.append(Square(int(line['Position']), p, width, height))

    def draw(self):
        board_color = arcade.color.BLACK
        board_center_x = self.SCREEN_WIDTH/2
        board_center_y = self.SCREEN_HEIGHT/2
        inner_board_width = (self.SCREEN_WIDTH-(self.EDGE_SPACE*2))*(3/4)
        inner_board_height = (self.SCREEN_HEIGHT-(self.EDGE_SPACE*2))*(3/4)
        outer_board_width = self.SCREEN_WIDTH-(self.EDGE_SPACE*2)
        outer_board_height = self.SCREEN_HEIGHT-(self.EDGE_SPACE*2)
        border_width = 1
        
        tile_width = inner_board_width/9
        tile_height = outer_board_height/8
        num_tiles = 9
        
        row_tile_x = self.EDGE_SPACE+tile_height+(tile_width/2)
        bottom_tile_y = self.EDGE_SPACE+tile_height/2
        top_tile_y = self.SCREEN_HEIGHT-self.EDGE_SPACE-(tile_height/2)
        column_tile_y = self.EDGE_SPACE+tile_height+(tile_width/2)
        left_tile_x = self.EDGE_SPACE+tile_height/2
        right_tile_x = self.SCREEN_WIDTH-self.EDGE_SPACE-(tile_height/2)
        
        bottom_tile_tilt = 0
        right_tile_tilt = 90
        top_tile_tilt = 180
        left_tile_tilt = 270

        left_corners_x = self.EDGE_SPACE+tile_height/2
        bottom_corners_y = self.EDGE_SPACE+tile_height/2
        right_corners_x = self.SCREEN_WIDTH-self.EDGE_SPACE-(tile_height/2)
        top_corners_y = self.SCREEN_HEIGHT-self.EDGE_SPACE-(tile_height/2)

        #draw inner square of board
        arcade.draw_rectangle_filled(board_center_x, board_center_y, 
                                     inner_board_width, inner_board_height, 
                                     (204, 227, 199))

        #draw logo
        logo = arcade.load_texture("assets/logo.png")
        logo_scale = (inner_board_width*(3/4))/600
        logo_tilt_angle = -45
        arcade.draw_scaled_texture_rectangle(self.SCREEN_WIDTH/2, 
                                             self.SCREEN_HEIGHT/2,
                                             logo, logo_scale, logo_tilt_angle)

        #draw outer square of board
        arcade.draw_rectangle_outline(board_center_x, board_center_y,
                                      outer_board_width, outer_board_height, 
                                      board_color, border_width)

        #draw community chest
        arcade.draw_rectangle_outline((self.SCREEN_WIDTH/2)+(inner_board_width/4),
                                      (self.SCREEN_HEIGHT/2)+(inner_board_height/4),
                                      tile_width, tile_width*2, 
                                      board_color, 
                                      border_width, 
                                      logo_tilt_angle - 90)

        #draw chance
        arcade.draw_rectangle_outline((self.SCREEN_WIDTH/2)-(inner_board_width/4), 
                                      (self.SCREEN_HEIGHT/2)-(inner_board_height/4), 
                                      tile_width, tile_width*2, 
                                      board_color, 
                                      border_width, 
                                      logo_tilt_angle - 90)

        property = Property("test", "test", 0, [], 0, 0)

        #draw go tile at position 0
        self.squares[0].draw(left_corners_x, bottom_corners_y, bottom_tile_tilt)

        # call square for each tile in left column
        for i in range(1, num_tiles + 1):
            self.squares[i].draw(left_tile_x, column_tile_y, left_tile_tilt)

            column_tile_y += tile_width

        #draw jail tile at position 10
        self.squares[10].draw(left_corners_x, top_corners_y, bottom_tile_tilt)

        # call square for each tile in top row
        for i in range(11, num_tiles + 11):
            self.squares[i].draw(row_tile_x, top_tile_y, top_tile_tilt)

            row_tile_x += tile_width

        #draw free parking tile at position 20
        self.squares[20].draw(right_corners_x, top_corners_y, bottom_tile_tilt)

        #reset column y
        column_tile_y = self.SCREEN_HEIGHT-self.EDGE_SPACE-(tile_height+(tile_width/2))

        # call square for each tile in right column
        for i in range(21, num_tiles + 21):
            self.squares[i].draw(right_tile_x, column_tile_y, right_tile_tilt)

            column_tile_y -= tile_width

        #draw go to jail at position 30
        self.squares[30].draw(right_corners_x, bottom_corners_y, bottom_tile_tilt)

        #reset row x
        row_tile_x = self.SCREEN_WIDTH-self.EDGE_SPACE-(tile_height+(tile_width/2))

        #call square for each tile in bottom row
        for i in range(31, num_tiles + 31):

            self.squares[i].draw(row_tile_x, bottom_tile_y, bottom_tile_tilt)

            row_tile_x -= tile_width

