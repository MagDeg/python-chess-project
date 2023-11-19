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
