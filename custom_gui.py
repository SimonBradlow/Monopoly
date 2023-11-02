import arcade
import arcade.gui

class BackgroundText(arcade.gui.UIWidget):
    def __init__(self, x = 0, y = 0, width = 100, height = 50, text = "", size_hint = None, size_hint_min = None, size_hint_max = None, style = None, **kwargs):
        super().__init__(x, y, width, height, size_hint=size_hint, size_hint_min=size_hint_min, size_hint_max=size_hint_max, style=style)
        self.text = text
        self.style = style or {}

    def do_render(self, surface: arcade.gui.Surface):
        self.prepare_render(surface)
        
        font_name = self.style.get("font_name", ("calibri", "arial"))
        font_size = self.style.get("font_size", 15)
        font_color = self.style.get("font_color", arcade.color.WHITE)
        border_width = self.style.get("border_width", 2)
        border_color = self.style.get("border_color", None)
        bg_color = self.style.get("bg_color", (21, 19, 21))

        if bg_color:
            arcade.draw_xywh_rectangle_filled(0, 0, self.width, self.height, color=bg_color)
        
        if border_color and border_width:
            arcade.draw_xywh_rectangle_outline(
                border_width,
                border_width,
                self.width - 2 * border_width,
                self.height - 2 * border_width,
                color=border_color,
                border_width=border_width)
        
        if self.text:
            start_x = self.width // 2
            start_y = self.height // 2

            text_margin = 2
            arcade.draw_text(
                text=self.text,
                start_x=start_x,
                start_y=start_y,
                font_name=font_name,
                font_size=font_size,
                color=font_color,
                align="center",
                anchor_x='center', anchor_y='center',
                width=self.width - 2 * border_width - 2 * text_margin
            )