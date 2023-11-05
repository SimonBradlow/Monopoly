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
            self.edge = self.width*0.075
            self.rgb_values = [(134, 76, 56), (172, 220, 242), (197, 56, 132), (236, 139, 44), (219, 36, 40), (255, 239, 3), (19, 168, 87), (0, 102, 164)]
            self.color_dict = {self.color_names[i]: self.rgb_values[i] for i in range(len(self.color_names))}

            background = arcade.create_rectangle_filled(0, 0, self.width, self.height, arcade.color.WHITE) 
            border = arcade.create_rectangle_outline(0, 0, self.width-self.edge, self.height-self.edge, arcade.color.BLACK, 1) 
            inner = arcade.create_rectangle_filled(0, ((self.height-self.edge*2)/10)*4, self.width-self.edge*2, (self.height-self.edge*2)/5, self.color_dict[self.group])
            inner_outline = arcade.create_rectangle_outline(0, ((self.height-self.edge*2)/10)*4, self.width-self.edge*2, (self.height-self.edge*2)/5, arcade.color.BLACK, 1)

            self.shape_list = arcade.ShapeElementList()
            self.shape_list.append(background)
            self.shape_list.append(border)
            self.shape_list.append(inner)
            self.shape_list.append(inner_outline)

            # Name Text
            self.deed_title = arcade.create_text_sprite(
                "T I T L E   D E E D", 
                0, 
                0, 
                arcade.color.BLACK, 
                14,
                font_name = "assets/KabelMediumRegular.ttf",
                align="center",
                anchor_x="center", 
                anchor_y="center",
            )
            fixed_name = self.name.upper().replace("AVENUE", "AVE.")
            self.name_text = arcade.create_text_sprite(
                fixed_name, 
                0, 
                0, 
                arcade.color.BLACK, 
                20,
                font_name = "assets/KabelMediumRegular.ttf",
                align="center",
                anchor_x="center", 
                anchor_y="center",
            )
            self.deed_title.scale = (self.height/4)/115
            self.name_text.scale = (self.height/4)/115

            # Rent Text
            rent_string = "RENT $" + str(self.rents[0]) + "\n"
            for i in range(1, 5):
                rent_string += "With " + str(i) + " House"
                if i != 1:
                    rent_string += "s"
                rent_string += "        $"
                rent_string += str(self.rents[i]) + "\n"
            rent_string += "With HOTEL $" + str(self.rents[i]) + "\n\n"
            rent_string += "Mortgage Value $" + str(self.price//2) + "\n"
            rent_string += "Houses cost $" + str(self.building_cost) + ". each\n"
            rent_string += "Hotels, $" + str(self.building_cost) + ". plus 4 houses\n"
            self.rent_text = arcade.create_text_sprite(
                rent_string, 
                0, 
                0, 
                arcade.color.BLACK, 
                20,
                font_name = "assets/KabelMediumRegular.ttf",
                align="center",
                anchor_x="center", 
                anchor_y="center",
            )

            self.rent_text.scale = (self.height/4)/135

            # Extra text
            group_string = "If a player owns ALL the Lots of any\n"
            group_string += "Color - Group the rent is Doubled on\n"
            group_string += "Unimproved Lots in that group"
            self.group_text = arcade.create_text_sprite(
                group_string, 
                0, 
                0, 
                arcade.color.BLACK, 
                14,
                font_name = "assets/KabelMediumRegular.ttf",
                align="center",
                anchor_x="center", 
                anchor_y="center",
            )
            self.group_text.scale = (self.height/4)/145

    def draw(self, x, y):
        if self.group in self.color_names:
            # Set position and rotation of tile
            self.shape_list.center_x = x
            self.shape_list.center_y = y

            # Draw the shape_list
            self.shape_list.draw()

            self.deed_title.center_x = x
            self.deed_title.center_y = y+(((self.height-self.edge*2)/20)*9)
            self.deed_title.draw()

            self.name_text.center_x = x
            self.name_text.center_y = y+(((self.height-self.edge*2)/80)*29)
            self.name_text.draw()

            self.rent_text.center_x = x
            self.rent_text.center_y = y-(((self.height-self.edge*2)/40)*3)
            self.rent_text.draw()

            self.group_text.center_x = x
            self.group_text.center_y = y-(((self.height-self.edge*2)/20)*9)
            self.group_text.draw()

        else:
            pass
