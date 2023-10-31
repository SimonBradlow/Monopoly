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

        self.carPiece.on_click = self.render_board
        self.dogPiece.on_click = self.render_board
        self.hatPiece.on_click = self.render_board
        self.shipPiece.on_click = self.render_board

    def render_board(self, event):

        game_view = GameView(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE)
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

    def __init__(self, w, h, e):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)
        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e
        self.sprite_list = arcade.sprite_list
        self.tiles = list[self.sprite_list]
        self.displayTile = 0

        # If you have sprite lists, you should create them here,
        # and set them to None

    def on_show_view(self):
        self.board = Board(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE)

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

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        # This is where you would check the win condition for GameOverView()
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
"""
    def on_mouse_press(self, x, y, button, key_modifiers):
        # Called when the user presses a mouse button. 
        print("here")
        # Get list of cards we've clicked on
        self.tiles = arcade.get_sprites_at_point((x, y), self.board.squares)

        # Have we clicked on a card?
        if len(self.tiles) > 0:

            # All other cases, grab the face-up card we are clicking on
            self.displayTile = self.tiles[0]

        if len(self.tiles) == 0:
            return

        tile_view = PropertyView(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE, self.tiles)
        self.window.show_view(tile_view)

"""
# GAME OVER SCREEN VIEW
class GameOverView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", self.width/2 - 200, 400, arcade.color.WHITE, 54)
        arcade.draw_text("U suck!", self.width/2 - 50, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         self.width / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")
