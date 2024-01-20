import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Rook(BaseFigure):

    def check_movement_allowance(self, field, fields):
        # returns true if move is valid and false if it is not

        # defining local variables for the target
        x = field.x
        y = field.y

        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)

        # if there is a figure between target and current field movement is not allowed
        if self.is_figure_on_line_straight(field, fields) is True:
            return False

        # rook can only move in straight lines
        if (delta_x == 0 and delta_y != 0) or (delta_x != 0 and delta_y == 0):
            return True

        return False
