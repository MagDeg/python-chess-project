import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Rook(BaseFigure):

    def check_movement_allowance(self, field, fields):

        x = field.x
        y = field.y

        if self.is_figure_on_line_straight(field, fields) is True:
            return False

        _delta_x = abs(self.x - x)
        _delta_y = abs(self.y - y)

        if (_delta_x == 0 and _delta_y != 0) or (_delta_x != 0 and _delta_y == 0):
            return True
        return False
