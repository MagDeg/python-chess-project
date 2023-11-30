import pygame

from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Knight(BaseFigure):
    def __init__(self, _color, start_x, start_y):
        super().__init__(_color, start_x, start_y)
        color = Color()
        if _color == color.WHITE:
            self.img = pygame.image.load("images/white_knight.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/black_knight.png").convert_alpha()

    def check_movement_allowance(self,field):
        x = field.x
        y = field.y

        _delta_x = abs(self.start_x - x)
        _delta_y = abs(self.start_y - y)
        if (_delta_x == 2 and _delta_y == 1) or (_delta_x == 1 and _delta_y == 2):
            return True
        return False
