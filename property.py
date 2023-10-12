class Property():
    """
    Class representing properties in Monopoly
    """
    def __init__(self, name: str, price: int, rents: list, building_cost: int, mortgage_value: int, mortgaged: bool = False, building_count: int = 0):
        self.name = name
        self.price = price
        self.rents = rents
        self.building_cost = building_cost
        self.mortgage_value = mortgage_value
        self.mortgaged = mortgaged
        self.building_count = building_count


    def draw(self):
        pass