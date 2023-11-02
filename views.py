import arcade
import arcade.gui
import arcade.texture
from PIL import Image
from player import Player
from board import Board

# START SCREEN VIEW
class StartView(arcade.View):

    def __init__(self, w, h, e):
        super().__init__()

        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e
        self.player_piece = 0

        # Create UI manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.update_buttons()

        # Create button textures
        self.carImage = Image.open('assets/car.png')
        self.carTexture = arcade.Texture(name="car", image=self.carImage)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome to Monopoly!", self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2 + 100,
                         arcade.color.WHITE_SMOKE, font_size=40, anchor_x="center")
        arcade.draw_text("Choose your piece", self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

        self.manager.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
          pass

    def update_buttons(self):
        self.manager.clear()

        #create buttons for piece selection
        self.carPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="car", image=Image.open('assets/car.png')), width=150, height=150,
                                           x=self.SCREEN_WIDTH/3 - 75, y=self.SCREEN_HEIGHT/4 - 25)
        self.dogPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="dog", image=Image.open('assets/dog.png')), width=100, height=100,
                                           x=self.SCREEN_WIDTH/3 + 150, y=self.SCREEN_HEIGHT/4)
        self.hatPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="hat", image=Image.open('assets/hat.png')), width=100, height=100,
                                           x=self.SCREEN_WIDTH/3 - 50, y=self.SCREEN_HEIGHT/4 - 150)
        self.shipPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="ship", image=Image.open('assets/ship.png')), width=200,
                                                    height=200, x=self.SCREEN_WIDTH/3 + 100, y=self.SCREEN_HEIGHT/4 - 185)

        self.manager.add(self.carPiece)
        self.manager.add(self.dogPiece)
        self.manager.add(self.hatPiece)
        self.manager.add(self.shipPiece)

        self.carPiece.on_click = self.on_click_car
        self.dogPiece.on_click = self.on_click_dog
        self.hatPiece.on_click = self.on_click_hat
        self.shipPiece.on_click = self.on_click_ship

    def on_click_car(self, event):
        self.player_piece = 0
        self.render_board()
    def on_click_dog(self, event):
        self.player_piece = 1
        self.render_board()
    def on_click_hat(self, event):
        self.player_piece = 2
        self.render_board()
    def on_click_ship(self, event):
        self.player_piece = 3
        self.render_board()
    def render_board(self):
        game_view = GameView(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE, self.player_piece)
        game_view.setup()
        self.window.show_view(game_view)


# PROPERTY CARD VIEW(?)
class PropertyView(arcade.View):

    def __init__(self, w, h, e, tile):
        super().__init__()

        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e
        self.tileToView = tile
    def on_show_view(self):

        arcade.set_background_color(arcade.color.AMAZON)
    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome to Monopoly!", self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2,
                         arcade.color.WHITE_SMOKE, font_size=40, anchor_x="center")
        arcade.draw_text("Click to advance", self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")


class GameView(arcade.View):
    """
    Main game/board class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, w, h, e, p):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)
        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e
        self.sprite_list = arcade.sprite_list
        self.tiles = list[self.sprite_list]
        self.displayTile = 0
        self.player_piece = p

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.board = Board(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE)

        # Game information to track
        self.board.players = [Player(0, self.player_piece, self.board.tile_width)]
        self.properties = self.board.properties
        self.owners = self.board.owners
        self.turn = 0
        self.doubles = 0
        self.rolled = 0
        self.rent_to_pay = False
        self.rent_owed = 0
        self.active_player = self.board.players[0]

        # Create UI manager
        self.button_width = 200
        self.button_height = 50
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.update_buttons()


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        self.board.draw()

        if type(self.active_player) is Player:
            self.manager.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        # This is where you would check the win condition for GameOverView()

        # Check which player's turn it is
        self.active_player = self.board.players[self.turn % len(self.board.players)]

        # If human turn, handle human interaction
        if type(self.active_player) is Player:
            pass

        # If computer turn, handle computer interaction
        else:
            pass

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

    def on_roll_dice(self, event):
        roll = self.board.roll()
        self.rolled += 1
        if roll[0] == roll[1]:
            self.doubles +=1
        if self.doubles >= 3:
            self.send_to_jail(self.active_player)
        else:
            self.board.move_player(self.active_player, roll[0] + roll[1])
        self.update_buttons()

    def on_end_turn(self, event):
        self.rolled = 0
        self.doubles = 0
        self.turn += 1
        self.update_buttons()

    def update_buttons(self):
        self.manager.clear()
        left_layout = arcade.gui.UIBoxLayout(vertical=True, x=0, y=100)
        # Add action button (roll or end turn)
        if self.rolled <= self.doubles:
            action = arcade.gui.UIFlatButton(text="Roll Dice", width=self.button_width, height=self.button_height)
            action.on_click = self.on_roll_dice
        else:
            action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height)
            action.on_click = self.on_end_turn
        left_layout.add(action)
        # Add square action (buy property, pay rent, draw card, pay taxes)
        square = None
        if self.rolled > 0:
            if self.board.squares[self.active_player.position].property.group == "Tax":
                # Pay taxes
                square = arcade.gui.UIFlatButton(text="Pay Taxes", width=self.button_width, height=self.button_height)
            elif self.board.squares[self.active_player.position].property.group in ["Chance", "Chest"]:
                # Draw a card
                square = arcade.gui.UIFlatButton(text="Draw a card", width=self.button_width, height=self.button_height)
            elif self.board.squares[self.active_player.position].property.group not in ['Go', 'Jail', 'Parking', 'GoToJail']:
                property_name = self.board.squares[self.active_player.position].property.name
                if self.owners[self.board.squares[self.active_player.position].property] is None:
                    # Buy the property
                    square = arcade.gui.UIFlatButton(text=f"Buy {property_name}", width=self.button_width, height=self.button_height)
                elif self.owners[self.board.squares[self.active_player.position].property] == self.active_player:
                    # Grey out buy button
                    square = arcade.gui.UILabel(text=f"Buy {property_name}", width=self.button_width, height=self.button_height)
                else:
                    # Pay rent
                    square = arcade.gui.UIFlatButton(text="Pay Rent", width=self.button_width, height=self.button_height)
        if square is not None:
            left_layout.add(square)
        self.manager.add(left_layout)
    
    def send_to_jail(self, player):
        pass

"""
# GAME OVER SCREEN VIEW
class GameOverView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        
        Draw Game over across the screen.
        
        arcade.draw_text("Game Over", self.width/2 - 200, 400, arcade.color.WHITE, 54)
        arcade.draw_text("U suck!", self.width/2 - 50, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         self.width / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")
"""