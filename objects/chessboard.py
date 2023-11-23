from objects.singlefield import *


class Chessboard:
    def __init__(self, _surface):
        self.surface = _surface

        self.fields = []
        for x in range(0, 8):
            column = []
            for y in range(0, 8):
                column.append(SingleField(x, y))

            self.fields.append(column)

    def draw(self, surface):
        for column in self.fields:
            for row in column:
                row.draw(surface)

    def check_mouse_position(self, _mouse_pos):
        for x in self.fields:
            for y in x:
                x_start = y.x * y.w
                y_start = y.y * y.h
                x_end = x_start + y.w
                y_end = y_start + y.h

                mouse_x = _mouse_pos[0]
                mouse_y = _mouse_pos[1]

                if x_start < mouse_x < x_end:
                    if y_start < mouse_y < y_end:
                        return y.x, y.y
