class Card():
    """
    Class representing an individual card.
    """
    def __init__(self, card_type: str = "", name: str = "", desc: str = "", category: str = "", effect: int = 0):
        self.card_type = card_type
        self.name = name
        self.desc = desc
        self.category = category
        self.effect = effect

    def get_name(self):
        return self.name

    def get_card_type(self):
        return self.card_type

    def get_desc(self):
        return self.desc

    def get_category(self):
        return self.category

    def get_effect(self):
        return self.effect

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
        if category == "money" or category == "money_players" or category == "money_houses":
            return (category, int(self.effect))
        elif category == "move" or category == "move_jail" or category == "move_utility" or category == "move_rr" or category == "move_abs":
            position = self.calculate_position(position)
            return (category, int(position))
        else:
            return (category, 1)