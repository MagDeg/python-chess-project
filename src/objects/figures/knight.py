import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Knight(BaseFigure):
    def __init__(self, color, start_x, start_y):
        # calling ParentClass's init method
        super().__init__(color, start_x, start_y)
        # loading image depending on color of figure
        if color == Color.WHITE:
            self.img = pygame.image.load("images/white_knight.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/black_knight.png").convert_alpha()

    def check_movement_allowance(self, field, fields):
        x = field.x
        y = field.y

        delta_x = abs(self.start_x - x)
        delta_y = abs(self.start_y - y)
        if (delta_x == 2 and delta_y == 1) or (delta_x == 1 and delta_y == 2):
            return True
        return False

