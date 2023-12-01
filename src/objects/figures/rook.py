import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Rook(BaseFigure):
    def __init__(self, color, start_x, start_y):
        super().__init__(color, start_x, start_y)
        if color == Color.WHITE:
            self.img = pygame.image.load("images/white_rook.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/black_rook.png").convert_alpha()

    def check_movement_allowance(self,field):

        x = field.x
        y = field.y

        _delta_x = abs(self.start_x - x)
        _delta_y = abs(self.start_y - y)

        if (_delta_x == 0 and _delta_y != 0) or (_delta_x != 0 and _delta_y == 0):
            return True
        return False



