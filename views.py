import arcade
import arcade.gui
import arcade.texture
from PIL import Image

import board
from player import Player
from computer_player import ComputerPlayer
from board import Board
import custom_gui
import random
from game import Game
import time

# Global variables used to measure game's time length
start_time = 0
end_time = 0
time_taken = 0

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
        arcade.draw_text("Welcome to", self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 200,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        # draw logo
        logo = arcade.load_texture("assets/logo.png")
        logo_scale = self.SCREEN_WIDTH / 2500
        logo_tilt_angle = 0
        arcade.draw_scaled_texture_rectangle(self.SCREEN_WIDTH / 2,
                                             self.SCREEN_HEIGHT / 2 + 100,
                                             logo, logo_scale, logo_tilt_angle)
        arcade.draw_text("Please Choose your piece", self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2 - 25,
                         arcade.color.WHITE_SMOKE, font_size=20, anchor_x="center")

        self.manager.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
          pass

    def update_buttons(self):
        self.manager.clear()
        width = self.SCREEN_WIDTH/8
        height = self.SCREEN_HEIGHT/8

        #create buttons for piece selection
        self.carPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="car", image=Image.open('assets/car.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8,
x=((self.SCREEN_WIDTH/8)-(width/2)), y=(((self.SCREEN_HEIGHT/8)*3)-50))
        self.dogPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="dog", image=Image.open('assets/dog.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8,
x=((self.SCREEN_WIDTH/8)*3)-(width/2), y=(((self.SCREEN_HEIGHT/8)*3)-(height/2)))
        self.hatPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="hat", image=Image.open('assets/hat.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8,
x=((self.SCREEN_WIDTH/8)*5)-(width/2), y=(((self.SCREEN_HEIGHT/8)*3)-(height/2)))
        self.shipPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="ship", image=Image.open('assets/ship.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8,
x=((self.SCREEN_WIDTH/8)*7)-(width/2), y=((self.SCREEN_HEIGHT/8)*3)-(height/2))
        self.bootPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="boot", image=Image.open('assets/boot.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8,
x=((self.SCREEN_WIDTH/8)-(width/2)), y=((self.SCREEN_HEIGHT/8)-(height/2)))
        self.ironPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="iron", image=Image.open('assets/iron.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8,
x=((self.SCREEN_WIDTH/8)*3)-(width/2), y=((self.SCREEN_HEIGHT/8)-(height/2)))
        self.thimblePiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="thimble", image=Image.open('assets/thimble.png')), width=self.SCREEN_WIDTH/8, height=self.SCREEN_HEIGHT/8,
x=((self.SCREEN_WIDTH/8)*5)-(width/2), y=((self.SCREEN_HEIGHT/8)-(height/2)))
        self.wheelbarrowPiece = arcade.gui.UITextureButton(texture=arcade.Texture(name="wheelbarrow", image=Image.open('assets/wheelbarrow.png')), width=self.SCREEN_WIDTH/8,
height=self.SCREEN_HEIGHT/8, x=((self.SCREEN_WIDTH/8)*7)-(width/2), y=((self.SCREEN_HEIGHT/8)-(height/2)))

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
        self.manager.remove(self.carPiece)
        self.manager.remove(self.dogPiece)
        self.manager.remove(self.hatPiece)
        self.manager.remove(self.shipPiece)
        self.manager.remove(self.bootPiece)
        self.manager.remove(self.ironPiece)
        self.manager.remove(self.thimblePiece)
        self.manager.remove(self.wheelbarrowPiece)
        global start_time
        start_time = time.time()
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

        # variables needed for displaying properties and buying house
        self.cannot_buy_house = arcade.gui.UIFlatButton()
        self.button_width = 200
        self.button_height = 50
        self.active_property = 0
        self.card_x = 0
        self.card_y = 0

        # identify color names for streets
        self.color_names = ['Brown', 'LightBlue', 'Pink', 'Orange', 'Red', 'Yellow', 'Green', 'Blue']

        # Create UI manager
        self.buy_house = None
        self.mortgage_button = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # new list for sorting properties
        self.property_group = []

        # Sort properties together by group
        for index in range(0, len(self.player.properties)):
            if self.player.properties[index].group == "Railroad":
                self.property_group.append(-1)
            elif self.player.properties[index].group == "Utility":
                self.property_group.append(0)
            else:
                if self.player.properties[index].group == "Brown":
                    self.property_group.append(1)
                if self.player.properties[index].group == "LightBlue":
                    self.property_group.append(2)
                if self.player.properties[index].group == "Pink":
                    self.property_group.append(3)
                if self.player.properties[index].group == "Orange":
                    self.property_group.append(4)
                if self.player.properties[index].group == "Red":
                    self.property_group.append(5)
                if self.player.properties[index].group == "Yellow":
                    self.property_group.append(6)
                if self.player.properties[index].group == "Green":
                    self.property_group.append(7)
                if self.player.properties[index].group == "Blue":
                    self.property_group.append(8)

        self.player.properties.sort(key=dict(zip(self.player.properties, self.property_group)).get)

        # Sprite for owning no houses
        self.no_owned_houses = arcade.create_text_sprite(
            "You do not own any \nproperties at this time.",
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2,
            arcade.color.WHITE,
            20,
            font_name="assets/KabelMediumRegular.ttf",
            align="center",
            anchor_x="center",
            anchor_y="center",
        )

        # Sprite for not being able to buy a house on property
        self.monopoly_info = arcade.create_text_sprite(
            "*You may only buy a house on a property \n"
            "if you have a monopoly over that color - group*",
            self.SCREEN_WIDTH / 2,
            (self.SCREEN_HEIGHT / 5),
            arcade.color.WHITE,
            10,
            font_name="assets/KabelMediumRegular.ttf",
            align="center",
            anchor_x="center",
            anchor_y="center",
        )

        # Sprite for escaping to game
        self.escape_info = arcade.create_text_sprite(
            "Press 'esc' to return to game.",
            self.SCREEN_WIDTH / 2,
            (self.SCREEN_HEIGHT/15),
            arcade.color.WHITE,
            15,
            font_name="assets/KabelMediumRegular.ttf",
            align="center",
            anchor_x="center",
            anchor_y="center",
        )

        self.update_buttons()

    def on_show_view(self):
        self.manager.enable()
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        # set where a card is initially rendered in the property view
        self.card_x = self.SCREEN_WIDTH / 2
        self.card_y = self.SCREEN_HEIGHT / 2

        if len(self.player.properties) == 0:
            self.no_owned_houses.draw()
        else:
            # Draw first property the player holds
            self.player.properties[self.active_property].draw(self.card_x, self.card_y)
            self.monopoly_info.draw()
            self.manager.draw()

        self.escape_info.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # if player presses esc button the view returns to board.
        if symbol == 65307:
            self.manager.disable()
            self.window.show_view(self.game_view)

    def update_buttons(self):
        if self.buy_house is not None:
            self.manager.remove(self.buy_house)
        if self.mortgage_button is not None:
            self.manager.remove(self.mortgage_button)

        # draw buy house button
        if len(self.player.properties) > 0:
            if self.player.properties[self.active_property].group in self.color_names:
                if self.game_view.game.can_buy_house(self.player.properties[self.active_property], self.player):
                    # Button for buying a house
                    self.buy_house = arcade.gui.UIFlatButton(text="Buy house", width=self.button_width,
                                                             height=self.button_height,
                                                             x=self.SCREEN_WIDTH / 2 - (self.button_width / 2),
                                                             y=self.SCREEN_HEIGHT - (self.button_height * 2))
                    self.manager.add(self.buy_house)
                    self.buy_house.on_click = self.buy_building
            # Draw mortgage property button
            if self.game_view.game.can_mortgage(self.player.properties[self.active_property]):
                self.mortgage_button = arcade.gui.UIFlatButton(text="Mortgage Property", width=self.button_width,
                                                               height=self.button_height,
                                                               x=self.SCREEN_WIDTH / 2 + (self.button_width / 2),
                                                               y=self.SCREEN_HEIGHT - (self.button_height * 2))
                self.manager.add(self.mortgage_button)
                self.mortgage_button.on_click = self.mortgage_property
            elif self.game_view.game.can_unmortgage(self.player.properties[self.active_property], self.player):
                self.mortgage_button = arcade.gui.UIFlatButton(text="Unmortgage Property", width=self.button_width,
                                                               height=self.button_height,
                                                               x=self.SCREEN_WIDTH / 2 + (self.button_width / 2),
                                                               y=self.SCREEN_HEIGHT - (self.button_height * 2))
                self.manager.add(self.mortgage_button)
                self.mortgage_button.on_click = self.unmortgage_property

        # Texture Button for scrolling right
        self.right_arrow = arcade.gui.UITextureButton(
            texture=arcade.Texture(name="right arrow", image=Image.open('assets/right_arrow.png')),
            width=self.SCREEN_WIDTH / 10,
            height=self.SCREEN_HEIGHT / 10, x=self.SCREEN_WIDTH - (self.SCREEN_WIDTH / 10),
            y=self.SCREEN_HEIGHT / 2)

        # Texture button for scrolling left
        self.left_arrow = arcade.gui.UITextureButton(
            texture=arcade.Texture(name="left arrow", image=Image.open('assets/left_arrow.png')),
            width=self.SCREEN_WIDTH / 10,
            height=self.SCREEN_HEIGHT / 10, x=(self.SCREEN_WIDTH / 30),
            y=self.SCREEN_HEIGHT / 2)

        self.manager.add(self.left_arrow)
        self.manager.add(self.right_arrow)

        self.left_arrow.on_click = self.scroll_left
        self.right_arrow.on_click = self.scroll_right

    def mortgage_property(self, event):
        self.game_view.game.mortgage(self.player.properties[self.active_property], self.player)
        self.update_buttons()

    def unmortgage_property(self, event):
        self.game_view.game.unmortgage(self.player.properties[self.active_property], self.player)
        self.update_buttons()

    def buy_building(self, event):

        self.game_view.game.buy_house(self.player.properties[self.active_property], self.player)
        self.update_buttons()

    def on_update(self, delta_time: float):

        if len(self.player.properties) == 0:
            pass
        else:
            # Draw first property the player holds
            self.player.properties[self.active_property].draw(self.card_x, self.card_y)



    def scroll_left(self, event):

        # if looking at property that isn't first in list
        if self.active_property > 0:
            # look at previous property
            self.active_property -= 1

        else:
            pass
        self.update_buttons()

    def scroll_right(self, event):

        # if property isn't last in list
        if self.active_property < len(self.player.properties)-1:
            # look at next property
            self.active_property += 1
        else:
            pass
        self.update_buttons()


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


        # Game information to track
        self.board.players = [Player(0, self.player_piece, self.board.tile_width), ComputerPlayer(1, 7 if self.player_piece != 7 else 0, self.board.tile_width)]
        self.game = Game(self.board.players, self.board.squares, self.board.owners, w)
        self.active_player = self.board.players[0]
        self.chat = []

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
        self.manager.enable()

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
        self.game.die_sprites.draw()
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

        # Player funds text interface
        fund_list = arcade.SpriteList()
        width = 0
        for i in range(len(self.board.players)):
            num = str(self.board.players[i].player_no+1)
            funds = str(self.board.players[i].money)
            fund_string = "p" + num + "\n$" + funds

            fund_sprite = arcade.create_text_sprite(
                fund_string, 
                16+(i*(width+16)), 
                self.SCREEN_HEIGHT, 
                arcade.color.BLACK, 
                16,
                font_name = "assets/KabelMediumRegular.ttf",
                align="center",
                anchor_x="left", 
                anchor_y="top",
            )
            width = fund_sprite.width
            fund_list.append(fund_sprite)
        fund_list.draw()

        # Chat log text interface
        if len(self.chat) > 0:
            log_sprite = arcade.create_text_sprite(
                "\n".join(self.chat[0]), 
                self.SCREEN_WIDTH, 
                self.SCREEN_HEIGHT, 
                arcade.color.WHITE, 
                16,
                font_name = "assets/KabelMediumRegular.ttf",
                align="right",
                anchor_x="right", 
                anchor_y="top",
            )
            log_sprite.scale = (self.SCREEN_WIDTH/2)/log_sprite.width
            log_sprite.center_x = self.SCREEN_WIDTH-5-(log_sprite.width/2)
            log_sprite.center_y = self.SCREEN_HEIGHT-5-(log_sprite.height/2)
            log_sprite.draw()

        if self.game.card is not None:
            self.game.card.draw()

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
        if type(self.game.active_player) is ComputerPlayer:
            self.game.active_player.take_turn(self.game)
            self.chat.clear()
            self.chat.append(self.board.players[1].log)
            self.update_buttons()

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
                if s.property in self.board.players[1].properties:
                    s.collision_sprite.color = (255,0,0,200)
                    s.property.render = True
                else:
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
        if self.game.card is not None:
            self.game.card = None
        else:
            pass

    def on_roll_dice(self, event):
        roll = self.game.roll_move()
        
        #chat log of dice rolls
        self.chat.clear()
        log_entry = []
        entry_string = "You have rolled ["
        first = True
        for num in roll:
            entry_string += str(num)
            if first:
                entry_string += ", "
            first = False
        entry_string += "], moving to "
        entry_string += self.board.squares[self.game.active_player.position].property.name
        log_entry.append(entry_string)
        self.chat.append(log_entry)

        self.update_buttons()

    def on_end_turn(self, event):
        if self.game.end_turn() == -1:
            self.manager.disable()
            global end_time
            end_time = time.time()
            end_view = GameOverView(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE)
            end_view.setup()
            self.window.show_view(end_view)
        else:
            self.update_buttons()
    
    def on_buy_property(self, event):
        self.game.buy_property(self.game.active_property(), self.game.active_player)
        entry = "You have bought "
        entry += self.board.squares[self.game.active_player.position].property.name
        entry += " for "
        entry += str(self.board.squares[self.game.active_player.position].property.price)
        self.chat[0].append(entry)
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
        self.manager.disable()
        property_view = PropertyView(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE, self.active_player)
        self.window.show_view(property_view)

    def on_roll_jail(self, event):
        self.game.roll_jail()
        self.update_buttons()

    def on_pay_fine(self, event):
        self.game.pay_fine()
        self.update_buttons()
    
    def on_card_jail(self, event):
        self.game.card_jail()
        self.update_buttons()

    def update_buttons(self):
        unclickable_style = {"bg_color_pressed": arcade.color.BLACK, "border_color_pressed": arcade.color.BLACK, "font_color_pressed": arcade.color.WHITE}
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
            roll_action = arcade.gui.UIFlatButton(text="You have made your roll", width=self.button_width, height=self.button_height, style=unclickable_style)
            pay_action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height)
            pay_action.on_click = self.on_end_turn
            self.left_layout.add(roll_action)
            self.left_layout.add(pay_action)
        else:
            # Add action button (roll or end turn)
            if "roll_move" in required_actions:
                action = arcade.gui.UIFlatButton(text="Roll Dice", width=self.button_width, height=self.button_height)
                action.on_click = self.on_roll_dice
            elif "roll_move" in stubs:
                action = arcade.gui.UIFlatButton(text="Roll Dice", height=self.button_height, width=self.button_width, style=unclickable_style)
            elif "end_turn" in required_actions:
                action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height)
                action.on_click = self.on_end_turn
            elif "end_turn" in stubs:
                action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height, style=unclickable_style)
            self.left_layout.add(action)
            # Add square action (buy property, pay rent, draw card, pay taxes)
            square = None
            if "pay_tax" in required_actions:
                # Pay taxes
                square = arcade.gui.UIFlatButton(text="Pay Taxes", width=self.button_width, height=self.button_height)
                square.on_click = self.on_pay_taxes
            elif "pay_tax" in stubs:
                square = arcade.gui.UIFlatButton(text="You have paid your tax!", width=self.button_width, height=self.button_height, style=unclickable_style)
            if "draw_card" in required_actions:
                # Draw a card
                square = arcade.gui.UIFlatButton(text="Draw a card", width=self.button_width, height=self.button_height)
                square.on_click = self.on_draw_card
            elif "draw_card" in stubs:
                square = arcade.gui.UIFlatButton(text="You have drawn your card!", width=self.button_width, height=self.button_height, style=unclickable_style)
            if "own_property" in stubs or "buy_property" in other_actions:
                property_name = self.game.active_property().name
                if "buy_property" in other_actions:
                    # Buy the property
                    square = arcade.gui.UIFlatButton(text=f"Buy {property_name}", width=self.button_width, height=self.button_height)
                    square.on_click = self.on_buy_property
                elif "own_property" in stubs:
                    # Grey out buy button
                    square = arcade.gui.UIFlatButton(text=f"You own {property_name}", width=self.button_width, height=self.button_height, style=unclickable_style)
            if "pay_rent" in required_actions:
                # Pay rent
                square = arcade.gui.UIFlatButton(text=f"Pay ${self.game.rent_owed} Rent", width=self.button_width, height=self.button_height)
                square.on_click = self.on_pay_rent
            elif "pay_rent" in stubs:
                square = arcade.gui.UIFlatButton(text=f"No rent owed!", width=self.button_width, height=self.button_height, style=unclickable_style)
            if square is not None:
                self.left_layout.add(square)
        self.manager.add(self.left_layout)

        # Manage the buttons on the right side of the screen
        self.manager.remove(self.right_layout)
        self.right_layout = arcade.gui.UIBoxLayout(vertical=True, x=self.SCREEN_WIDTH-self.button_width, y=100)
        property_button = arcade.gui.UIFlatButton(text="View Properties", width=self.button_width, height=self.button_height)
        property_button.on_click = self.on_view_properties
        self.right_layout.add(property_button)

        # Add button to use get out of jail free card if it is an option
        if "card_jail" in other_actions:
            card_button = arcade.gui.UIFlatButton(text="Get Out Of Jail Free!", width=self.button_width, height=self.button_height)
            card_button.on_click = self.on_card_jail
            self.right_layout.add(card_button)
        self.manager.add(self.right_layout)




# GAME OVER SCREEN VIEW
class GameOverView(arcade.View):

    def __init__(self, w, h, e):
        super().__init__()

        arcade.set_background_color(arcade.color.AMAZON)
        self.SCREEN_HEIGHT = h
        self.SCREEN_WIDTH = w
        self.EDGE_SPACE = e
        global time_taken
        time_taken = end_time - start_time

    def setup(self):
        pass
    def on_show_view(self):
        pass

    def on_draw(self):
        self.clear()
        
        arcade.draw_text("Game Over!", self.SCREEN_WIDTH/2 - 200, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Thanks for playing!", self.SCREEN_WIDTH/2 - 140, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(time_taken, 2)} seconds"
        arcade.draw_text(f"Game time: {time_taken_formatted}",
                         self.SCREEN_WIDTH / 2,
                         200,
                         arcade.color.WHITE,
                         font_size=15,
                         anchor_x="center")


