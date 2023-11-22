from player import Player
import arcade

class Card():
    """
    Class representing an individual card.
    """
    def __init__(self, card_type: str = "", name: str = "", desc: str = "", category: str = "", effect: int = 0, scale: int = 800):
        self.card_type = card_type
        self.name = name
        self.desc = desc
        self.category = category
        self.effect = effect

        # Global constants used for drawing cards
        self.sprite_list = arcade.SpriteList()

        if card_type == "Chance":
            card_color = (255, 95, 0)
        else:
            card_color = (255, 215, 0)
        background = arcade.SpriteSolidColor(int(scale/2), int(scale/4), card_color)
        background.center_x = scale/2
        background.center_y = scale/2

        fixed_desc = desc.replace('.', '\n')
        text = card_type +'\n\n'+ name +'\n'+ fixed_desc
        text_sprite = arcade.create_text_sprite(
            text, 
            scale/2, 
            scale/2, 
            arcade.color.BLACK, 
            20,
            font_name = "assets/KabelMediumRegular.ttf",
            align="center",
            anchor_x="center", 
            anchor_y="center",
        )
        if text_sprite.width > ((scale/2)-10):
            text_sprite.scale = ((scale/2)-10)/text_sprite.width

        self.sprite_list.append(background)
        self.sprite_list.append(text_sprite)

    def calculate_position(self, position, player: Player):
        # Determine where player needs to move, calculate how far they need to
        # move from their current position
        name = self.name
        if 'Go' in name:
            player.money += 200
            return 0
        elif 'Illinois Ave.' in name:
            if position > 24:
                player.money += 200
            return 24
        elif 'St. Charles Place' in name:
            if position > 11:
                player.money += 200
            return 11
        elif 'nearest Utility' in name:
            electric_company = 12
            water_works = 28

            if position < electric_company or position > water_works:
                if position > water_works:
                    player.money += 200
                return electric_company
            else:
                return water_works
        elif 'nearest Railroad' in name:
            rr = 5
            pr = 15
            bor = 25
            sl = 35

            if position < rr or position > sl:
                if position > sl:
                    player.money += 200
                return rr
            elif position < pr:
                return pr
            elif position < bor:
                return bor
            else:
                return sl
        elif 'Go Back 3 Spaces' in name:
            return -3
        elif 'Go to Jail' in name:
            return 10
        elif 'Reading Railroad' in name:
            if position > 5:
                player.money += 200
            return 5
        elif 'Boardwalk' in name:
            return 39

    def return_effect(self, position, player: Player):
        category = self.category
        if category == "money" or category == "money_players":
            return (category, int(self.effect))
        elif category == "money_houses":
            if self.card_type == "Chance":
                return (category, -25, -100)
            else:
                return (category, -40, -115)
        elif category == "move" or category == "move_jail" or category == "move_utility" or category == "move_rr" or category == "move_abs":
            position = self.calculate_position(position, player)
            return (category, int(position))
        else:
            return (category, 1)

    def draw(self):
        self.sprite_list.draw()
