from functions.draw import PygameUtils
from functions.get_screen_size import ScreenSize
from functions.color import Color


class SingleField:
    # class for every single field of chessboard

    def __init__(self, x, y):
        # getting screen size
        screen_size = ScreenSize()

        # passing position of field
        self.x = x
        self.y = y

        # getting width and height (field is square -> height = width) of field
        self.w = screen_size.get_single_field_size()
        self.h = self.w

        # variable for figure on field
        self.figure = None
        # variable for color of field
        self.color = None

        # color is defined according to the coordinates
        # if both coordinates are dividable by two it is a black field
        if (self.x + self.y) % 2 == 0:
            self.color = Color.FIELD_BLACK
        # if not it is a white field
        else:
            self.color = Color.FIELD_WHITE

    def set_hover_color(self):
        # updating color to hover color if field was selected
        # according to current color
        if self.color == Color.FIELD_WHITE:
            self.color = Color.FIELD_SELECTED_WHITE
        else:
            self.color = Color.FIELD_SELECTED_BLACK

    def remove_hover_color(self):
        # updating color to original color if field was unselected
        # according to current color
        if self.color == Color.FIELD_SELECTED_WHITE:
            self.color = Color.FIELD_WHITE
        else:
            self.color = Color.FIELD_BLACK

    def set_figure(self, figure):
        # function to set figure to a field
        self.figure = figure

    def get_figure(self):
        # function to return figure of field
        return self.figure

    def _draw_figure(self, x, y, surface):
        # drawing figure if it is not none, to position
        if self.figure is None:
            return
        # drawing figure by its own draw function
        self.figure.draw(x, y, surface, self.w)

    def draw(self, surface):
        # drawing field

        # getting real screen coordinates by multiplying chessboard coordinates with width of single field
        x1 = self.x * self.w
        y1 = self.y * self.h

        # drawing field with pygame draw function on surface
        PygameUtils.draw_rect(self.color, x1, y1, self.w, self.h, surface)

        # drawing figure on field
        self._draw_figure(self.x, self.y, surface)
