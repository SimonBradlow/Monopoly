import arcade
from views import StartView

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
EDGE_SPACE = 100
SCREEN_TITLE = "Monopoly!"

# MAIN GAME VIEW
def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartView(SCREEN_WIDTH, SCREEN_HEIGHT, EDGE_SPACE)
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
