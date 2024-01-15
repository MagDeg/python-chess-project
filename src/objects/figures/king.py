from objects.figures.base_figure import BaseFigure
from functions.color import Color
import pygame
from objects.figures.rook import Rook


class King(BaseFigure):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def _change_moved(self):
        # change moved variable from false to true
        if self.moved is False:
            self.moved = True
            return

    def check_movement_allowance(self, field, fields):
        x = field.x
        y = field.y

        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)

        # if king has not been moved, it can make a castling
        if self.moved is False:
            # there it can move two fields and change his position with the rook
            if delta_y == 0 and delta_x == 2:
                # it has to be checked on which side the king moves by comparing target-x and selected-x to get
                # the position of the rook
                if self.x > x:
                    # if the rook is on the left side of the king it is a field more away,
                    # because of the position of the queen
                    field_next_to_target = fields[x-2][y]
                else:
                    field_next_to_target = fields[x+1][y]
                # getting figure on the field
                figure_next_to_target = field_next_to_target.get_figure()
                # checking if figure is a rook and has not been moved either
                if figure_next_to_target.moved is False and type(figure_next_to_target) is Rook:
                    # if there is no figure in between
                    if self.is_figure_on_line_straight(field, fields) is False:
                        # return special event
                        return "castling"

        if (delta_x == delta_y == 1) or (delta_x == 0 and delta_y == 1) or (delta_x == 1 and delta_y == 0):
            return True
        return False

    def draw(self, x, y, surface, size):
        # function to draw the figure on the field
        # if figure is moved the first, the variable moved will be refreshed to true
        if not (self.x == x and self.y == y):
            self._change_moved()

        self.refresh_current_position(x, y)

        # actual draw method, but first resize to the SingleFiled size
        surface.blit(pygame.transform.scale(self.img, (size, size)), (x * size, y * size))
