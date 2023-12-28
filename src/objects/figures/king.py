from objects.figures.base_figure import BaseFigure
from functions.color import Color
import pygame


class King(BaseFigure):
    def __init__(self, color, start_x, start_y):
        super().__init__(color, start_x, start_y)
        if color == Color.WHITE:
            self.img = pygame.image.load("images/white_king.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/black_king.png").convert_alpha()

    def check_movement_allowance(self, field, fields):
        x = field.x
        y = field.y

        delta_x = abs(self.start_x - x)
        delta_y = abs(self.start_y - y)
        if (delta_x == delta_y == 1) or (delta_x == 0 and delta_y == 1) or (delta_x == 1 and delta_y == 0):
            return True
        return False
