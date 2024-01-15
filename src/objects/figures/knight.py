import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Knight(BaseFigure):
    def __init__(self, color, x, y):
        # calling ParentClass's init method
        super().__init__(color, x, y)

    def check_movement_allowance(self, field, fields):
        # returns true if move is valid and false if it is not

        # fields has to be passed as parameter, because in other figure classes it is used in the function

        # defining local variables for the target
        x = field.x
        y = field.y

        # calculation difference between actual position and target position for x and y
        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)

        # the knight is only allowed to move in "L"-shaped patterns so either
        # delta_x == 2 and delta_y == 1 or delta_x == 1 and delta_y == 2
        if (delta_x == 2 and delta_y == 1) or (delta_x == 1 and delta_y == 2):
            return True
        return False

