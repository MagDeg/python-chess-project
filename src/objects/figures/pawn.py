import pygame.image
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Pawn(BaseFigure):

    def __init__(self, color, x, y):
        # calling ParentClass's init method
        super().__init__(color, x, y)

    def check_movement_allowance(self, field, fields):
        # returns true if move is valid and false if it is not

        # defining target field variables
        x = field.x
        y = field.y

        # calculating the difference between target and current field
        delta_x = (self.x - x)
        delta_y = (self.y - y)

        # detecting if there is an enemy on the target field, because it changes the movement allowance
        # (only by the pawn)
        enemy_on_field = self.check_field_for_enemy(field)

        if enemy_on_field is False:
            # if there is now enemy the pawn can only move straight forward

            # checking if there is a figure inbetween that would be an obstacle
            if self.is_figure_on_line_straight(field, fields) is True:
                return False

            # if the figure has not been moved it can move one or two fields ahead,
            # so the x level is not allowed to change
            if delta_x == 0:
                if self.moved is False:
                    # making difference between black and white figures,
                    # because black figures can only move in the negative direction of the y-axis -> has to be negative
                    # and white figure can only move in the positive direction of the y-axis -> has to be positive
                    if (self.color == Color.BLACK and (delta_y == 1 or delta_y == 2)) or (
                            self.color == Color.WHITE and (delta_y == -1 or delta_y == -2)):
                        return True
                else:
                    # if the figure was already moved it can only be moved one field ahead
                    if (self.color == Color.BLACK) and (delta_y == 1):
                        return True
                    if (self.color == Color.WHITE) and (delta_y == -1):
                        return True
        else:
            # if there is an enemy on the field the pawn is allowed to move one step diagonal
            if (delta_x == 1 or delta_x == -1) and delta_y == 1 and self.color == Color.BLACK:
                return True
            if (delta_x == -1 or delta_x == 1) and delta_y == -1 and self.color == Color.WHITE:
                return True
        return False

    def _change_moved(self):
        # change moved variable from false to true
        if self.moved is False:
            self.moved = True
            return

    def draw(self, x, y, surface, size):
        # function to draw the figure on the field
        # if figure is moved the first, the variable moved will be refreshed to true
        if not (self.x == x and self.y == y):
            self._change_moved()

        self.refresh_current_position(x, y)

        # actual draw method, but first resize to the SingleFiled size
        surface.blit(pygame.transform.scale(self.img, (size, size)), (x * size, y * size))

