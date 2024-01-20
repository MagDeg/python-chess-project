import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Queen(BaseFigure):

    def check_movement_allowance(self, field, fields):
        # returns true if move is valid and false if it is not

        # defining local variables for the target
        x = field.x
        y = field.y

        # calculating delta of target and current position
        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)

        # queen allowed to move diagonal, so deltas have to be equal and can not be 0
        if delta_x == delta_y != 0:
            # if there is a figure between target and current field movement is not allowed
            if self.is_figure_on_line_diagonal(field, fields) is True:
                return False

            return True
        # queen is also allowed to move in straight lines
        if (delta_x == 0 and delta_y != 0) or (delta_x != 0 and delta_y == 0):
            # if there is a figure between target and current field movement is not allowed
            if self.is_figure_on_line_straight(field, fields) is True:
                return False

            return True

        return False

