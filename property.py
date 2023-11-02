import arcade

class Property():
    """
    Class representing properties in Monopoly
    """
    def __init__(self, name: str, group:str, price: int, rents: list, building_cost: int, mortgage_value: int, mortgaged: bool = False, building_count: int = 0):
        """
        Initializer for Property class
        """
        self.name = name
        self.group = group
        self.price = price
        self.rents = rents
        self.building_cost = building_cost
        self.mortgage_value = mortgage_value
        self.mortgaged = mortgaged
        self.building_count = building_count

        self.render = False
        self.width = 0
        self.height = 0
        self.color_names = ['Brown', 'LightBlue', 'Pink', 'Orange', 'Red', 'Yellow', 'Green', 'Blue']
        if self.group in self.color_names:      
            self.width = 200
            self.height = self.width*1.125
            edge = self.width*0.075
            self.rgb_values = [(134, 76, 56), (172, 220, 242), (197, 56, 132), (236, 139, 44), (219, 36, 40), (255, 239, 3), (19, 168, 87), (0, 102, 164)]
            self.color_dict = {self.color_names[i]: self.rgb_values[i] for i in range(len(self.color_names))}

            background = arcade.create_rectangle_filled(0, 0, self.width, self.height, arcade.color.WHITE) 
            border = arcade.create_rectangle_outline(0, 0, self.width-edge, self.height-edge, arcade.color.BLACK, 1) 
            inner = arcade.create_rectangle_filled(0, ((self.height-edge*2)/8)*3, self.width-edge*2, (self.height-edge*2)/4, self.color_dict[self.group])
            inner_outline = arcade.create_rectangle_outline(0, ((self.height-edge*2)/8)*3, self.width-edge*2, (self.height-edge*2)/4, arcade.color.BLACK, 1)

            self.shape_list = arcade.ShapeElementList()
            self.shape_list.append(background)
            self.shape_list.append(border)
            self.shape_list.append(inner)
            self.shape_list.append(inner_outline)

    def draw(self, x, y):
        if self.group in self.color_names:
            # Set position and rotation of tile
            self.shape_list.center_x = x
            self.shape_list.center_y = y

            # Draw the shape_list
            self.shape_list.draw()

        else:
            pass
