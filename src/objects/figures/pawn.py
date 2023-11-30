import pygame.image
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Pawn(BaseFigure):

    def __init__(self, _color, start_x, start_y):
        super().__init__(_color, start_x, start_y)
        color = Color()
        if _color == color.WHITE:
            self.img = pygame.image.load("images/white_pawn.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/black_pawn.png").convert_alpha()
        self.move = None

    def check_movement_allowance(self, field):

        x = field.x
        y = field.y

        _delta_x = (self.start_x - x)
        _delta_y = (self.start_y - y)

        color = Color()

        print(_delta_x, _delta_y)
        print(self.moved)
        if (self.moved is False or self.moved is None) and (_delta_x == 0):
            if (self.color == color.BLACK and (_delta_y == 1 or _delta_y == 2)) or (
                    self.color == color.WHITE and (_delta_y == -1 or _delta_y == -2)):
                print("true")
                return True
        else:
            if (self.color == color.BLACK) and (_delta_y == 1) and (_delta_x == 0):
                print("true")
                return True
            if (self.color == color.WHITE) and (_delta_y == -1) and (_delta_x == 0):
                print("true")
                return True
        print("false")
        return False

    def _change_moved(self):
        print("prechange:" + str(self.moved))
        if self.moved is None:
            self.moved = False
            return
        if self.moved is False:
            self.moved = True
            return

    def draw(self, x, y, surface, size):
        self._change_moved()
        self.start_x = x
        self.start_y = y
        surface.blit(pygame.transform.scale(self.img, (size, size)), (x * size, y * size))

