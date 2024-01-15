from functions.draw import PygameUtils
from functions.get_screen_size import ScreenSize
from functions.color import Color


class SingleField:
    def __init__(self, _x, _y):
        screen_size = ScreenSize()

        self.x = _x
        self.y = _y
        self.w = screen_size.get_single_field_size()
        self.h = self.w
        self.figure = None
        self.color = None

        if (self.x + self.y) % 2 == 0:
            self.color = Color.FIELD_BLACK
        else:
            self.color = Color.FIELD_WHITE

    def set_hover_color(self):
        if self.color == Color.FIELD_WHITE:
            self.color = Color.FIELD_SELECTED_WHITE
        else:
            self.color = Color.FIELD_SELECTED_BLACK

    def remove_hover_color(self):
        if self.color == Color.FIELD_SELECTED_WHITE:
            self.color = Color.FIELD_WHITE
        else:
            self.color = Color.FIELD_BLACK

    def set_figure(self, figure):
        self.figure = figure

    def get_figure(self):
        return self.figure

    def _draw_figure(self, x, y, surface):
        if self.figure is None:
            return
        self.figure.draw(x, y, surface, self.w)

    def draw(self, surface):

        x1 = self.x * self.w
        y1 = self.y * self.h

        PygameUtils.draw_rect(self.color, x1, y1, self.w, self.h, surface)

        self._draw_figure(self.x, self.y, surface)
