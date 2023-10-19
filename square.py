from property import Property
import arcade

class Square():
    """
    The class representing an individual square on the board
    """
    def __init__(self, position: int, property: Property, width: float, height: float):
        self.position = position
        self.property = property

        # CODE BELOW IS NEEDED FOR Square.draw() METHOD
        # Initialize shape_list
        self.shape_list = arcade.ShapeElementList()
        self.sprite_list = arcade.SpriteList()
        self.house_sprites = []

        # Create shape objects
        background = arcade.create_rectangle_filled(0, 0, width, height, (204, 227, 199)) 
        border = arcade.create_rectangle_outline(0, 0, width, height, arcade.color.BLACK, 1) 
        # TODO: translate color string into RGB and fill inner with it
        inner = arcade.create_rectangle_filled(0, (height/8)*3, width, height/4, arcade.color.BLUE)
        inner_outline = arcade.create_rectangle_outline(0, (height/8)*3, width, height/4, arcade.color.BLACK, 1)

        # Add shape objects to the shape_list
        self.shape_list.append(background)
        self.shape_list.append(border)
        if self.space == "Street":
            self.shape_list.append(inner)
            self.shape_list.append(inner_outline)

        # Initialize non-street sprites
        scaling = width/204
        sprite_names = ["go", "jail", "freeparking", "gotojail"]
        fixed_name = self.name.lower().replace(" ", "")
        if fixed_name in sprite_names:
            png_name = "assets/" + fixed_name + ".png"
            tile_sprite = arcade.Sprite(png_name, scaling)
            tile_sprite.center_x = 0
            tile_sprite.center_y = 0
            self.sprite_list.append(tile_sprite)

        # Initialize house sprites
        if property is not None:
            house_scaling = width/400 
            for i in range(5):
                png_name = "assets/house" + str(i+1) + ".png"
                self.house_sprites.append(arcade.Sprite(png_name, house_scaling))

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
        if self.property is not None:
            if self.property.building_count > 0:
                house = self.house_sprites[self.property.building_count-1]
                house.center_x = x
                house.center_y = y + (self.height/8)*3
                house.angle = angle
                house.position = arcade.rotate_point(
                    house.center_x, house.center_y,
                    x, y, angle)
                house.draw()
