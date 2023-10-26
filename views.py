import arcade

# START SCREEN VIEW
class StartView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome to Monopoly!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.WHITE_SMOKE, font_size=40, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        board_view = GameView()
        board_view.setup()
        self.window.show_view(board_view)

# PROPERTY CARD VIEW(?)
class PropertyView(arcade.View):
    def on_show_view(self):
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
