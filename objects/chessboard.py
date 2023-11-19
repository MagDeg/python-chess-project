from objects.field import *


class Chessboard:
    def __init__(self, _surface):
        self.surface = _surface

        self.fields = []
        for x in range(0, 8):
            row = []

            for y in range(0, 8):
                row.append(Field(x, y))

            self.fields.append(row)

    def draw(self, surface):
        for col in self.fields:
            for row in col:
                row.draw(surface)
