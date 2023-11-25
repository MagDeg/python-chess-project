from objects.figures.base_figure import BaseFigure
from functions.color import Color
from functions.draw import PygameLocal


class Pawn(BaseFigure):

    def check_movement_allowance(self, field):

        x = field.x
        y = field.y

        _delta_x = (self.start_x - x)
        _delta_y = (self.start_y - y)

        color = Color()

        print(_delta_x, _delta_y)

        if (self.moved == False) and (_delta_x == 0):
            if (self.color == color.BLACK and (_delta_y == 1 or _delta_y == 2)) or (self.color == color.WHITE and (_delta_y == -1 or _delta_y == -2)):
                print("true")
                return True
        else:
            if (self.color == color.BLACK) and (_delta_y == 1):
                return True
            if (self.color == color.WHITE) and (_delta_y == -1):
                return True
        return False


    def draw(self, x, y, surface):
        if not (self.start_x == x and self.start_y == y):
            # not on starting position
            self.moved = True
        self.start_x = x
        self.start_y = y
        # implement draw method



