import arcade
import arcade.gui
import arcade.texture
from PIL import Image

import board
from player import Player
from board import Board
import custom_gui
import random

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

        # variables needed for displaying properties and buying house
        self.buy_house = arcade.gui.UIFlatButton()
        self.left_arrow = arcade.gui.UITextureButton()
        self.right_arrow = arcade.gui.UITextureButton()
        self.button_width = 200
        self.button_height = 50
        self.active_property = 0
        self.card_x = 0
        self.card_y = 0

        # identify color names for streets
        self.color_names = ['Brown', 'LightBlue', 'Pink', 'Orange', 'Red', 'Yellow', 'Green', 'Blue']

        # Create UI manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.update_buttons()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        # set where a card is initially rendered in the property view
        self.card_x = self.SCREEN_WIDTH / 2
        self.card_y = self.SCREEN_HEIGHT / 2

        # Draw first property the player holds
        self.player.properties[self.active_property].draw(self.card_x, self.card_y)

        self.manager.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        # if player presses esc button the view returns to board.
        if symbol == 65307:

            self.window.show_view(self.game_view)

    def update_buttons(self):
        self.manager.clear()

        # draw buy house button
        self.buy_house = arcade.gui.UIFlatButton(text="Buy house", width=self.button_width, height=self.button_height,
                                                 x=self.SCREEN_WIDTH/2-(self.button_width/2), y=self.SCREEN_HEIGHT-(self.button_height*2))

        self.right_arrow = arcade.gui.UITextureButton(
            texture=arcade.Texture(name="right arrow", image=Image.open('assets/right_arrow.png')), width=self.SCREEN_WIDTH / 10,
            height=self.SCREEN_HEIGHT / 10, x=self.SCREEN_WIDTH - (self.SCREEN_WIDTH/10),
            y=self.SCREEN_HEIGHT/2)

        self.left_arrow = arcade.gui.UITextureButton(
            texture=arcade.Texture(name="left arrow", image=Image.open('assets/left_arrow.png')), width=self.SCREEN_WIDTH / 10,
            height=self.SCREEN_HEIGHT / 10, x=(self.SCREEN_WIDTH/30),
            y=self.SCREEN_HEIGHT/2)

        self.manager.add(self.buy_house)
        self.manager.add(self.left_arrow)
        self.manager.add(self.right_arrow)

        self.buy_house.on_click = self.buy_property
        self.left_arrow.on_click = self.scroll_left
        self.right_arrow.on_click = self.scroll_right

    def buy_property(self, event):

        # if type of property is a street
        if self.player.properties[self.active_property].group in self.color_names:
            # no more than four houses allowed on a property
            if self.player.properties[self.active_property].building_count <= 3:
                self.player.properties[self.active_property].building_count += 1

    def on_update(self, delta_time: float):

        # Draw first property the player holds
        self.player.properties[self.active_property].draw(self.card_x, self.card_y)

    def scroll_left(self, event):

        # if looking at property that isn't first in list
        if self.active_property > 0:
            # look at previous property
            self.active_property -= 1
        else:
            pass

    def scroll_right(self, event):

        # if property isn't last in list
        if self.active_property < len(self.player.properties)-1:
            # look at next property
            self.active_property += 1
        else:
            pass


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
        self.properties = self.board.properties
        self.owners = self.board.owners
        self.turn = 0
        self.doubles = 0
        self.rolled = 0
        self.taxes_to_pay = False
        self.card_to_draw = False
        self.rent_to_pay = False
        self.rent_owed = 0
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
        roll = self.board.roll()

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

        self.rolled += 1
        if roll[0] == roll[1]:
            self.doubles +=1
        if self.doubles >= 3:
            self.send_to_jail(self.active_player)
        else:
            self.board.move_player(self.active_player, roll[0] + roll[1])
            # Update game variables based on where the player ends up
            if self.board.squares[self.active_player.position].property.group == "Tax":
                self.taxes_to_pay = True
            elif self.board.squares[self.active_player.position].property.group in ["Chance", "Chest"]:
                self.card_to_draw = True
            elif self.board.squares[self.active_player.position].property.group not in ["Go", "Jail", "Parking", "GoToJail"]:
                if self.owners[self.board.squares[self.active_player.position].property] != self.active_player:
                    self.rent_owed = self.board.calculate_rent(self.board.squares[self.active_player.position].property, roll)
                    if self.rent_owed > 0:
                        self.rent_to_pay = True
        self.update_buttons()

    def on_end_turn(self, event):
        if self.active_player.jailtime > 0:
            self.active_player.jailtime += 1
        self.rolled = 0
        self.doubles = 0
        self.turn += 1
        self.update_buttons()
    
    def on_buy_property(self, event):
        prop = self.board.squares[self.active_player.position].property
        self.board.buy_property(prop, self.active_player)
        self.update_buttons()
    
    def on_pay_rent(self, event):
        prop = self.board.squares[self.active_player.position].property
        owner = self.owners[prop]
        self.active_player.money -= self.rent_owed
        owner.money += self.rent_owed
        self.rent_to_pay = False
        self.rent_owed = 0
        self.update_buttons()
    
    def on_pay_taxes(self, event):
        # Dummy function to pay taxes, doesn't actually remove money
        self.taxes_to_pay = False
        self.update_buttons()
    
    def on_draw_card(self, event):
        # Dummy function to draw card, removes flag but doesn't actually draw the card
        self.card_to_draw = False
        self.update_buttons()

    def on_view_properties(self, event):
        property_view = PropertyView(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.EDGE_SPACE, self.active_player)
        self.window.show_view(property_view)

    def on_roll_jail(self, event):
        # Roll dice to get out of jail
        dice = self.board.roll()
        self.rolled += 1
        if dice[0] == dice[1]:
            # If doubles are rolled, the player gets out of jail and moves that far
            self.active_player.jailtime = 0
            self.board.move_player(self.active_player, dice[0] + dice[1])
        elif self.active_player.jailtime > 3:
            # If the player has been in jail for 3 turns and fails to roll doubles, they must pay the fine and move
            self.active_player.money -= 50
            self.active_player.jailtime = 0
            self.board.move_player(self.active_player, dice[0] + dice[1])
        self.update_buttons()

    def on_pay_fine(self, event):
        # If the player chooses to pay their fine
        self.active_player.money -= 50
        self.active_player.jailtime = 0
        self.update_buttons()

    def update_buttons(self):
        # Remove the old buttons
        self.manager.remove(self.left_layout)
        # Create the new container for the left buttons
        self.left_layout = arcade.gui.UIBoxLayout(vertical=True, x=0, y=100)
        # Check if the player is in jail
        if self.active_player.jailtime > 0:
            if self.rolled == 0:
                roll_action = arcade.gui.UIFlatButton(text="Roll for Doubles", width=self.button_width, height=self.button_height)
                roll_action.on_click = self.on_roll_jail
                pay_action = arcade.gui.UIFlatButton(text="Pay your $50 Fine", width=self.button_width, height=self.button_height)
                pay_action.on_click = self.on_pay_fine
            else:
                roll_action = custom_gui.BackgroundText(text="You have made your roll", width=self.button_width, height=self.button_height)
                pay_action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height)
                pay_action.on_click = self.on_end_turn
            self.left_layout.add(roll_action)
            self.left_layout.add(pay_action)
        # If the player is not in jail, proceed normally
        else:
            # Add action button (roll or end turn)
            if self.rolled <= self.doubles and True not in [self.card_to_draw, self.rent_to_pay, self.taxes_to_pay]:
                action = arcade.gui.UIFlatButton(text="Roll Dice", width=self.button_width, height=self.button_height)
                action.on_click = self.on_roll_dice
            elif self.rolled <= self.doubles:
                action = custom_gui.BackgroundText(text="Roll Dice", height=self.button_height, width=self.button_width)
            elif True not in [self.card_to_draw, self.rent_to_pay, self.taxes_to_pay]:
                action = arcade.gui.UIFlatButton(text="End Turn", width=self.button_width, height=self.button_height)
                action.on_click = self.on_end_turn
            else:
                action = custom_gui.BackgroundText(text="End Turn", width=self.button_width, height=self.button_height)
            self.left_layout.add(action)
            # Add square action (buy property, pay rent, draw card, pay taxes)
            square = None
            if self.rolled > 0:
                if self.board.squares[self.active_player.position].property.group == "Tax" and self.taxes_to_pay:
                    # Pay taxes
                    square = arcade.gui.UIFlatButton(text="Pay Taxes", width=self.button_width, height=self.button_height)
                    square.on_click = self.on_pay_taxes
                elif self.board.squares[self.active_player.position].property.group == "Tax":
                    square = custom_gui.BackgroundText(text="You have paid your tax!", width=self.button_width, height=self.button_height)
                elif self.board.squares[self.active_player.position].property.group in ["Chance", "Chest"] and self.card_to_draw:
                    # Draw a card
                    square = arcade.gui.UIFlatButton(text="Draw a card", width=self.button_width, height=self.button_height)
                    square.on_click = self.on_draw_card
                elif self.board.squares[self.active_player.position].property.group in ["Chance", "Chest"]:
                    square = custom_gui.BackgroundText(text="You have drawn your card!", width=self.button_width, height=self.button_height)
                elif self.board.squares[self.active_player.position].property.group not in ['Go', 'Jail', 'Parking', 'GoToJail']:
                    property_name = self.board.squares[self.active_player.position].property.name
                    if self.owners[self.board.squares[self.active_player.position].property] is None:
                        # Buy the property
                        square = arcade.gui.UIFlatButton(text=f"Buy {property_name}", width=self.button_width, height=self.button_height)
                        square.on_click = self.on_buy_property
                    elif self.owners[self.board.squares[self.active_player.position].property] == self.active_player:
                        # Grey out buy button
                        square = custom_gui.BackgroundText(text=f"You own {property_name}", width=self.button_width, height=self.button_height)
                    else:
                        if self.rent_to_pay:
                            # Pay rent
                            square = arcade.gui.UIFlatButton(text=f"Pay ${self.rent_owed} Rent", width=self.button_width, height=self.button_height)
                            square.on_click = self.on_pay_rent
                        else:
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
    
    def send_to_jail(self, player: Player):
        # Set the player's position to in jail
        player.position = 10
        player.jailtime = 1




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
