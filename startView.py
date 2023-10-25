"""
startView file creates window and displays start screen until a button is pressed
"""
import arcade
import os
from board import Board

WIDTH = 600
HEIGHT = 600
TITLE = "Monopoly!"

class startView(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome to Monopoly!", WIDTH / 2, HEIGHT / 2,
                         arcade.color.WHITE_SMOKE, font_size=40, anchor_x="center")
        arcade.draw_text("Click to advance", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        board_view = Board()
        board_view.setup()
        self.window.show_view(board_view)

class propertyView(arcade.View):

    def on_show_view(self):
        pass

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    start_view = startView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()