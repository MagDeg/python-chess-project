import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Bishop(BaseFigure):

    def check_movement_allowance(self, field, fields):
        x = field.x
        y = field.y

        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)

        if self.is_figure_on_line_diagonal(field, fields) is True:
            return False

        if delta_x == delta_y != 0:
            return True
        return False
