import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Bishop(BaseFigure):

    def check_movement_allowance(self, field, fields):
        # returns true if move is valid and false if it is not

        # defining local variables for the target
        x = field.x
        y = field.y

        # calculating delta of target and current position
        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)

        # if there is a figure between target and current field movement is not allowed
        if self.is_figure_on_line_diagonal(field, fields) is True:
            return False

        # in order to move diagonal both deltas have to be the same and can not be 0
        if delta_x == delta_y != 0:
            return True

        return False
