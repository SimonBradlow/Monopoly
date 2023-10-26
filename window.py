import arcade
from board import Board
from views import StartView
from views import PropertyView
from views import GameOverView
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
EDGE_SPACE = 100
SCREEN_TITLE = "Monopoly!"

# MAIN GAME VIEW
class GameView(arcade.View):
    """
    Main game/board class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, EDGE_SPACE)

        # Game information to track
        self.players = []
        self.turn = 0
        self.doubles = 0
        self.rolled = False

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

        # Check which player's turn it is
        self.active_player = self.board.players[self.board.turn % len(self.board.players)]

        # If human turn, handle human interaction
        if type(self.active_player) is Player:
            # Determine where in the turn we are, and which buttons to draw
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


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    main()
