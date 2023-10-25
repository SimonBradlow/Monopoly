from property import Property
import arcade
import math

class Square():
    """
    The class representing an individual square on the board
    """
    def __init__(self, position: int, prop: Property, width: float, height: float):
        self.position = position
        self.property = prop
        self.width = width
        self.height = height

        # CODE BELOW IS NEEDED FOR Square.draw() METHOD
        # Initialize shape_list
        self.shape_list = arcade.ShapeElementList()
        self.sprite_list = arcade.SpriteList()
        self.house_sprites = []

        self.color_names = ['Brown', 'LightBlue', 'Pink', 'Orange', 'Red', 'Yellow', 'Green', 'Blue']
        self.rgb_values = [(134, 76, 56), (172, 220, 242), (197, 56, 132), (236, 139, 44), (219, 36, 40), (255, 239, 3), (19, 168, 87), (0, 102, 164)]
        self.color_dict = {self.color_names[i]: self.rgb_values[i] for i in range(len(self.color_names))}

        # Create shape objects
        background = arcade.create_rectangle_filled(0, 0, width, height, (204, 227, 199)) 
        border = arcade.create_rectangle_outline(0, 0, width, height, arcade.color.BLACK, 1) 
        self.shape_list.append(background)
        self.shape_list.append(border)

        # Fill inner square with property color
        if self.property.group in self.color_names:
            inner = arcade.create_rectangle_filled(0, (height/8)*3, width, height/4, self.color_dict[self.property.group])
            inner_outline = arcade.create_rectangle_outline(0, (height/8)*3, width, height/4, arcade.color.BLACK, 1)
            self.shape_list.append(inner)
            self.shape_list.append(inner_outline)

        # Initialize non-street sprites
        scaling = (width-1)/204
        sprite_names = ["go", "jail", "freeparking", "gotojail"]
        fixed_name = self.property.name.lower().replace(" ", "")
        if fixed_name in sprite_names:
            png_name = "assets/" + fixed_name + ".png"
            tile_sprite = arcade.Sprite(png_name, scaling)
            tile_sprite.center_x = 0
            tile_sprite.center_y = 0
            self.sprite_list.append(tile_sprite)

        # Initialize house sprites
        if self.property.group in self.color_names:
            house_scaling = width/400 
            for i in range(5):
                png_name = "assets/house" + str(i+1) + ".png"
                self.house_sprites.append(arcade.Sprite(png_name, house_scaling))

            # Text
            split_text = self.property.name.upper()
            split_text = "   " + split_text + "      $" + str(self.property.price)
            unsplit_text = split_text.replace(" ", "\n")
            self.nameText = arcade.create_text_sprite(
                unsplit_text, 
                0, 
                0, 
                arcade.color.BLACK, 
                20,
                font_name = "assets/KabelMediumRegular.ttf",
                align="center",
                anchor_x="center", 
                anchor_y="center",
            )
            self.nameText.scale = self.width/260

    def draw(self, x, y, angle):
        # Set position and rotation of tile
        self.shape_list.center_x = x
        self.shape_list.center_y = y
        self.shape_list.angle = angle

        # Draw the shape_list
        self.shape_list.draw()

        # Corner pieces
        # if self.property.name == "go"
        if self.width == self.height:
            for s in self.sprite_list:
                s.center_x = x
                s.center_y = y
                s.angle = angle
            self.sprite_list.draw()

        # House sprites
        if self.property.group in self.color_names:
            if self.property.building_count > 0:
                house = self.house_sprites[self.property.building_count-1]
                house.center_x = x
                house.center_y = y + (self.height/8)*3
                house.angle = angle
                house.position = arcade.rotate_point(
                    house.center_x, house.center_y,
                    x, y, angle)
                house.draw()

            # Draw name text sprite
            self.nameText.center_x = x
            self.nameText.center_y = y
            self.nameText.angle = angle
            self.nameText.draw()
