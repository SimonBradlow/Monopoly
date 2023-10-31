import arcade
import arcade.gui
from board import Board
from player import Player

# START SCREEN VIEW
class StartView(arcade.View):

    def __init__(self, w, h, e):
        super().__init__()

        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e

        arcade.set_background_color(arcade.color.AMAZON)

    #def on_show_view(self):



    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome to Monopoly!", self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2,
                         arcade.color.WHITE_SMOKE, font_size=40, anchor_x="center")
        arcade.draw_text("Click to advance", self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE)
        game_view.setup()
        self.window.show_view(game_view)

# PROPERTY CARD VIEW(?)
class PropertyView(arcade.View):
    def on_show_view(self):
        pass

class GameView(arcade.View):
    """
    Main game/board class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, EDGE_SPACE):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)
        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, EDGE_SPACE)

        # Game information to track
        self.players = [Player(0, self.board.tile_width)]
        self.properties = self.board.properties
        self.owners = self.board.owners
        self.turn = 0
        self.doubles = 0
        self.rolled = 0
        self.rent_to_pay = False
        self.rent_owed = 0
        self.active_player = None

        # Create UI manager
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
        self.active_player = self.players[self.turn % len(self.players)]

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
        if self.rolled <= self.doubles:
            action = arcade.gui.UIFlatButton(text="Roll Dice", width=200)
            action.on_click = self.on_roll_dice
        else:
            action = arcade.gui.UIFlatButton(text="End Turn", width=200)
            action.on_click = self.on_end_turn
        self.manager.add(action)
    
    def send_to_jail(self, player):
        pass

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
