import arcade
import arcade.gui
import arcade.texture
from PIL import Image

import board
from player import Player
from board import Board
import custom_gui
import random
from game import Game

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
        width = self.SCREEN_WIDTH/8
        height = self.SCREEN_HEIGHT/8

        #create buttons for piece selection
        self.carPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="car", image=Image.open('assets/car.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)-(width/2)), y=(((self.SCREEN_HEIGHT/8)*3)-50))
        self.dogPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="dog", image=Image.open('assets/dog.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)*3)-(width/2), y=(((self.SCREEN_HEIGHT/8)*3)-(height/2)))
        self.hatPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="hat", image=Image.open('assets/hat.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)*5)-(width/2), y=(((self.SCREEN_HEIGHT/8)*3)-(height/2)))
        self.shipPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="ship", image=Image.open('assets/ship.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)*7)-(width/2), y=((self.SCREEN_HEIGHT/8)*3)-(height/2))
        self.bootPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="boot", image=Image.open('assets/boot.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)-(width/2)), y=((self.SCREEN_HEIGHT/8)-(height/2)))
        self.ironPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="iron", image=Image.open('assets/iron.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)*3)-(width/2), y=((self.SCREEN_HEIGHT/8)-(height/2)))
        self.thimblePiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="thimble", image=Image.open('assets/thimble.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)*5)-(width/2), y=((self.SCREEN_HEIGHT/8)-(height/2)))
        self.wheelbarrowPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="wheelbarrow", image=Image.open('assets/wheelbarrow.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)*7)-(width/2), y=((self.SCREEN_HEIGHT/8)-(height/2)))

        self.manager.add(self.carPiece)
        self.manager.add(self.dogPiece)
        self.manager.add(self.hatPiece)
        self.manager.add(self.shipPiece)
        self.manager.add(self.bootPiece)
        self.manager.add(self.ironPiece)
        self.manager.add(self.thimblePiece)
        self.manager.add(self.wheelbarrowPiece)

        self.carPiece.on_click = self.on_click_car
        self.dogPiece.on_click = self.on_click_dog
        self.hatPiece.on_click = self.on_click_hat
        self.shipPiece.on_click = self.on_click_ship
        self.bootPiece.on_click = self.on_click_boot
        self.ironPiece.on_click = self.on_click_iron
        self.thimblePiece.on_click = self.on_click_thimble
        self.wheelbarrowPiece.on_click = self.on_click_wheelbarrow

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
    def on_click_boot(self, event):
        self.player_piece = 4
        self.render_board()
    def on_click_iron(self, event):
        self.player_piece = 5
        self.render_board()
    def on_click_thimble(self, event):
        self.player_piece = 6
        self.render_board()
    def on_click_wheelbarrow(self, event):
        self.player_piece = 7
        self.render_board()

    def render_board(self):
        game_view = GameView(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE, self.player_piece)
        game_view.setup()
        self.window.show_view(game_view)


# PROPERTIES VIEW
class PropertyView(arcade.View):

    def __init__(self, game_view, w, h, e, p):
        super().__init__()

        self.SCREEN_WIDTH = w
        self.SCREEN_HEIGHT = h
        self.EDGE_SPACE = e
        self.player = p
        self.game_view = game_view
        self.tile_width = 200
        self.tile_height = 225

        self.mouse_sprite = arcade.SpriteSolidColor(1, 1, (0, 0, 0, 0))

        #margins for scrolling through properties
        self.top_viewport_margin = 20
        self.bottom_viewport_margin = 20
        self.view_bottom = 0
        self.view_top = 0
        self.changed = False
        self.card_x = 0
        self.card_y = 0


    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        # set where a card is initially rendered in the property view
        self.card_x = self.tile_width/2
        self.card_y = self.SCREEN_HEIGHT-115

        # Placing cards on the screen, currently hard coded but
        # should be made more dynamic to fit varying window sizes eventually
        for i in range(0, len(self.player.properties)):
            # For the first 5 cards, put it in one column.
            if i <= 4:
                self.player.properties[i].draw(self.card_x, self.card_y)
            # Next 4(?) cards go in the next column.
            elif i > 4 and i <= 8:
                self.card_x += 200
                self.card_y = self.SCREEN_HEIGHT-115
                self.player.properties[i].draw(self.card_x, self.card_y)
            else:
                self.card_x += 200
                self.card_y = self.SCREEN_HEIGHT-115
                self.player.properties[i].draw(self.card_x, self.card_y)
            self.card_y -= 225
    def on_key_press(self, symbol: int, modifiers: int):
        # if player presses esc button the view returns to board.
        if symbol == 65307:
            # resetting view so board is rendered back in the center of the screen.
            arcade.set_viewport(self.view_top,
                                self.SCREEN_HEIGHT + self.view_top,
                                0,
                                self.SCREEN_HEIGHT)
            self.window.show_view(self.game_view)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):

        self.mouse_sprite.center_x = x
        self.mouse_sprite.center_y = y

        # set boundary for window scrolling
        self.top_boundary = self.view_bottom + self.SCREEN_HEIGHT - self.top_viewport_margin
        self.bottom_boundary = self.view_bottom + self.SCREEN_HEIGHT - self.bottom_viewport_margin

        # check if scroll up is needed
        if self.mouse_sprite.center_y > self.top_boundary:
            self.view_bottom += self.mouse_sprite.center_y - self.top_boundary
            self.changed = True

        # check if scroll down is needed
        if self.mouse_sprite.center_y < self.bottom_boundary:
            self.view_bottom -= self.bottom_boundary - self.mouse_sprite.center_y
            self.changed = True

        # if scroll is needed
        if self.changed:
            #cast viewport to integers so it doesn't mess with pixels
            self.view_bottom = int(self.view_bottom)
            self.view_top = int(self.view_top)

            # actually do the scroll
            arcade.set_viewport(self.view_top,
                                self.SCREEN_HEIGHT + self.view_top,
                                self.view_bottom,
                                self.SCREEN_HEIGHT + self.view_bottom)





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
        self.displayTile = 0
        self.player_piece = p

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.board = Board(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE)
        self.mouse_sprite = arcade.SpriteSolidColor(1, 1, (0,0,0,0))
        self.die_sprites = arcade.SpriteList()


        # Game information to track
        self.board.players = [Player(0, self.player_piece, self.board.tile_width)]
        self.game = Game(self.board.players, self.board.squares, self.board.owners)
        self.active_player = self.board.players[0]

        # Create UI manager
        self.button_width = 200
        self.button_height = 50
        self.manager = arcade.gui.UIManager()
        self.left_layout = arcade.gui.UIBoxLayout(vertical=True, x=0, y=100)
        self.right_layout = arcade.gui.UIBoxLayout(vertical=True, x=self.SCREEN_WIDTH-self.button_width, y=100)
        self.manager.enable()
        self.manager.add(self.left_layout)
        self.manager.add(self.right_layout)
        self.update_buttons()


    def on_show_view(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def setup(self):
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
        self.die_sprites.draw()
        for s in self.board.squares:
            if s.property.render == True:
                if self.mouse_sprite.center_x < self.SCREEN_WIDTH/2:
                    if self.mouse_sprite.center_y < self.SCREEN_HEIGHT/2:
                        s.property.draw(self.mouse_sprite.center_x+s.property.width/2, 
                                        self.mouse_sprite.center_y+s.property.height/2)
                    else:
                        s.property.draw(self.mouse_sprite.center_x+s.property.width/2, 
                                        self.mouse_sprite.center_y-s.property.height/2)
                else:
                    if self.mouse_sprite.center_y < self.SCREEN_HEIGHT/2:
                        s.property.draw(self.mouse_sprite.center_x-s.property.width/2, 
                                        self.mouse_sprite.center_y+s.property.height/2)
                    else:
                        s.property.draw(self.mouse_sprite.center_x-s.property.width/2, 
                                        self.mouse_sprite.center_y-s.property.height/2)

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
        self.active_player = self.board.players[self.game.turns % len(self.board.players)]

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
        self.mouse_sprite.center_x = x
        self.mouse_sprite.center_y = y
        for s in self.board.squares:
            if arcade.check_for_collision(s.collision_sprite, self.mouse_sprite):
                s.collision_sprite.color = (255,255,255,75)
                s.property.render = True
            else:
                s.collision_sprite.color = (0,0,0,0)
                s.property.render = False


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
        roll = self.game.roll_move()

        # DICE RENDER FUNCTIONALITY
        self.die_sprites.clear()
        die_list = []
        i = 0
        while i < 2:
            scaling = (self.board.tile_width/1.5)/350
            png_name = "assets/die" + str(roll[i]) + ".png"
            die_sprite = arcade.Sprite(png_name, scaling)
            rand_x = random.randint((self.board.tile_width*3)*(-1), self.board.tile_width*3)
            rand_y = random.randint((self.board.tile_width*3)*(-1), self.board.tile_width*3)
            die_sprite.center_x = self.SCREEN_WIDTH/2 + rand_x
            die_sprite.center_y = self.SCREEN_WIDTH/2 + rand_y
            die_sprite.angle = random.randint(0, 90)
            die_list.append(die_sprite)
            # Check for overlapping dice and restart if so
            if (i == 1) and (arcade.check_for_collision(die_list[0], die_list[1])):
                die_list.clear()
                i = 0
            else:
                i += 1
        for s in die_list:
            self.die_sprites.append(s)
        
        self.update_buttons()

    def on_end_turn(self, event):
        self.game.end_turn()
        self.update_buttons()
    
    def on_buy_property(self, event):
        self.game.buy_property(self.game.active_property(), self.game.active_player)
        self.update_buttons()
    
    def on_pay_rent(self, event):
        self.game.pay_rent()
        self.update_buttons()
    
    def on_pay_taxes(self, event):
        self.game.pay_tax()
        self.update_buttons()
    
    def on_draw_card(self, event):
        self.game.draw_card()
        self.update_buttons()

    def on_view_properties(self, event):
        property_view = PropertyView(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE, self.active_player)
        self.window.show_view(property_view)

    def on_roll_jail(self, event):
        self.game.roll_jail()
        self.update_buttons()

    def on_pay_fine(self, event):
        self.game.pay_fine()
        self.update_buttons()

    def update_buttons(self):
        # Remove the old buttons
        self.manager.remove(self.left_layout)
        # Create the new container for the left buttons
        self.left_layout = arcade.gui.UIBoxLayout(vertical=True, x=0, y=100)

        required_actions, other_actions, stubs = self.game.legal_actions()
        # Check if the player is in jail
        if "roll_jail" in required_actions and "pay_fine" in required_actions:
            roll_action = arcade.gui.UIFlatButton(text="Roll for Doubles", width=self.button_width, height=self.button_height)
            roll_action.on_click = self.on_roll_jail
            pay_action = arcade.gui.UIFlatButton(text="Pay your $50 Fine", width=self.button_width, height=self.button_height)
            pay_action.on_click = self.on_pay_fine
            self.left_layout.add(roll_action)
            self.left_layout.add(pay_action)
        elif "rolled_jail" in required_actions and "end_turn" in required_actions:
            roll_action = custom_gui.BackgroundText(text="You have made your roll", width=self.button_width, height=self.button_height)
            pay_action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height)
            pay_action.on_click = self.on_end_turn
            self.left_layout.add(roll_action)
            self.left_layout.add(pay_action)
        # Add action button (roll or end turn)
        if "roll_move" in required_actions:
            action = arcade.gui.UIFlatButton(text="Roll Dice", width=self.button_width, height=self.button_height)
            action.on_click = self.on_roll_dice
        elif "roll_move" in stubs:
            action = custom_gui.BackgroundText(text="Roll Dice", height=self.button_height, width=self.button_width)
        elif "end_turn" in required_actions:
            action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height)
            action.on_click = self.on_end_turn
        elif "end_turn" in stubs:
            action = custom_gui.BackgroundText(text="End Turn", width=self.button_width, height=self.button_height)
        self.left_layout.add(action)
        # Add square action (buy property, pay rent, draw card, pay taxes)
        square = None
        if "pay_tax" in required_actions:
            # Pay taxes
            square = arcade.gui.UIFlatButton(text="Pay Taxes", width=self.button_width, height=self.button_height)
            square.on_click = self.on_pay_taxes
        elif "pay_tax" in stubs:
            square = custom_gui.BackgroundText(text="You have paid your tax!", width=self.button_width, height=self.button_height)
        if "draw_card" in required_actions:
            # Draw a card
            square = arcade.gui.UIFlatButton(text="Draw a card", width=self.button_width, height=self.button_height)
            square.on_click = self.on_draw_card
        elif "draw_card" in stubs:
            square = custom_gui.BackgroundText(text="You have drawn your card!", width=self.button_width, height=self.button_height)
        if "own_property" in stubs or "buy_property" in other_actions:
            property_name = self.game.active_property().name
            if "buy_property" in other_actions:
                # Buy the property
                square = arcade.gui.UIFlatButton(text=f"Buy {property_name}", width=self.button_width, height=self.button_height)
                square.on_click = self.on_buy_property
            elif "own_property" in stubs:
                # Grey out buy button
                square = custom_gui.BackgroundText(text=f"You own {property_name}", width=self.button_width, height=self.button_height)
        if "pay_rent" in required_actions:
            # Pay rent
            square = arcade.gui.UIFlatButton(text=f"Pay ${self.game.rent_owed} Rent", width=self.button_width, height=self.button_height)
            square.on_click = self.on_pay_rent
        elif "pay_rent" in stubs:
            square = custom_gui.BackgroundText(text=f"No rent owed!", width=self.button_width, height=self.button_height)
        if square is not None:
            self.left_layout.add(square)
        self.manager.add(self.left_layout)

        # Manage the buttons on the right side of the screen
        self.manager.remove(self.right_layout)
        self.right_layout = arcade.gui.UIBoxLayout(vertical=True, x=self.SCREEN_WIDTH-self.button_width, y=100)
        property_button = arcade.gui.UIFlatButton(text="View Properties", width=self.button_width, height=self.button_height)
        property_button.on_click = self.on_view_properties
        self.right_layout.add(property_button)
        self.manager.add(self.right_layout)




# GAME OVER SCREEN VIEW
class GameOverView(arcade.View):

    def __init__(self, w, h, e):
        super.__init__()

        arcade.set_background_color(arcade.color.BLACK)
        self.SCREEN_HEIGHT = w
        self.SCREEN_WIDTH = h
        self.EDGE_SPACE = e

    def setup(self):
        pass
    def on_show_view(self):
        pass

    def on_draw(self):
        self.clear()
        
        arcade.draw_text("Game Over", self.width/2 - 200, 400, arcade.color.WHITE, 54)
        arcade.draw_text("U suck!", self.width/2 - 50, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         self.width / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")
