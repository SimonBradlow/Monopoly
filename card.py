import arcade

class Card():
    """
    Class representing an individual card.
    """
    def __init__(self, card_type: str = "", name: str = "", desc: str = "", category: str = "", effect: int = 0, scale: int = 600):
        self.card_type = card_type
        self.name = name
        self.desc = desc
        self.category = category
        self.effect = effect

        # Global constants used for drawing cards
        self.sprite_list = arcade.SpriteList()
        background = arcade.SpriteSolidColor(scale/2, scale/4, (255, 95, 0))
        background.center_x = scale/2
        background.center_y = scale/2
        self.sprite_list.append(background)

    def calculate_position(self, position):
        # Determine where player needs to move, calculate how far they need to
        # move from their current position
        name = self.name
        if 'Go' in name:
            return 0
        elif 'Illinois Ave.' in name:
            return 24
        elif 'St. Charles Place' in name:
            return 11
        elif 'nearest Utility' in name:
            electric_company = 12
            water_works = 28

            if position < electric_company or position > water_works:
                return electric_company
            else:
                return water_works
        elif 'nearest Railroad' in name:
            rr = 5
            pr = 15
            bor = 25
            sl = 35

            if position < rr or position > sl:
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
            return 5
        elif 'Boardwalk' in name:
            return 39

    def return_effect(self, position):
        category = self.category
        if category == "money" or category == "money_players":
            return (category, int(self.effect))
        elif category == "money_houses":
            if self.card_type == "Chance":
                return (category, -25, -100)
            else:
                return (category, -40, -115)
        elif category == "move" or category == "move_jail" or category == "move_utility" or category == "move_rr" or category == "move_abs":
            position = self.calculate_position(position)
            return (category, int(position))
        else:
            return (category, 1)

    def draw(self):
        self.sprite_list.draw()
