from objects.figures.base_figure import BaseFigure


class Pawn(BaseFigure):

    def movement_allowed(self, x, y):
        _delta_x = (self.start_x - x)
        _delta_y = (self.start_y - y)
        if (self.moved == False) and (_delta_x == 0):
            if self.color == "Black" and (_delta_y == 1 or _delta_y == 2) or \
                    (self.color == "White" and (_delta_y == -1 or _delta_y == -2)):
                return True
        else:
            if (self.color == "Black") and (_delta_y == 1):
                return True
            if (self.color == "White") and (_delta_y == -1):
                return True
        return False

    def move(self, x, y):
        if self.movement_allowed(x, y):
            if not self.moved:
                self.moved = True
            # move figure
