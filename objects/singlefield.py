from functions.draw import PygameLocal
from functions.get_screen_size import ScreenSize
from functions.color import Color


class SingleField:
    def __init__(self, _x, _y):
        screen_size = ScreenSize()

        self.x = _x
        self.y = _y
        self.w = int(screen_size.get_single_field_size())
        self.h = self.w
        self.figure = 0

    def set_figure(self, _figure):
        self.figure = _figure

    def check_figure(self):
        return self.figure

    def draw(self, surface):
        color_ref = Color()
        x1 = self.x * self.w
        y1 = self.y * self.h

        if (self.x + self.y) % 2 == 0:
            color = color_ref.FIELD_BLACK
        else:
            color = color_ref.FIELD_WHITE

        pygame_local = PygameLocal(surface)
        pygame_local.drawRect(color, x1, y1, self.w, self.h)
