from property import Property
import arcade

class Square():
    """
    The class representing an individual square on the board
    """
    def __init__(self, name: str, property: Property, x: int, y: int, width: float, height: float):
        self.name = name
        self.property = property
        self.x = x
        self.y = y

        # CODE BELOW IS NEEDED FOR Square.draw() METHOD
        # Initialize shape_list
        self.shape_list = arcade.ShapeElementList()

        # Create shape objects
        background = arcade.create_rectangle_filled(0, 0, width, height, arcade.color.MINT) 
        border = arcade.create_rectangle_outline(0, 0, width, height, arcade.color.BLACK, 2) 
        inner = arcade.create_rectangle_filled(0, (height/8)*3, width, height/4, arcade.color.BLUE)
        inner_outline = arcade.create_rectangle_outline(0, (height/8)*3, width, height/4, arcade.color.BLACK, 2)

        # Add objects to the shape_list
        self.shape_list.append(background)
        self.shape_list.append(border)
        self.shape_list.append(inner)
        self.shape_list.append(inner_outline)

    def draw(self, x, y, angle):
        # Set position and rotation of tile
        self.shape_list.center_x = x
        self.shape_list.center_y = y
        self.shape_list.angle = angle

        # Draw the shape_list
        self.shape_list.draw()
