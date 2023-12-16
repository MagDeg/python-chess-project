import pygame
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Rook(BaseFigure):
    def __init__(self, color, start_x, start_y):
        super().__init__(color, start_x, start_y)
        if color == Color.WHITE:
            self.img = pygame.image.load("images/white_rook.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/black_rook.png").convert_alpha()

    def check_movement_allowance(self, field, fields):

        x = field.x
        y = field.y

        if self.start_x > x:
            for i in range(x, self.start_x):
                if self.start_y > y:
                    for j in range(y, self.start_y):
                        print(fields[i][j].get_figure())
                        if fields[i][j].get_figure() is not None:
                            return False
                elif self.start_y < y:
                    for j in range(self.start_y, y):
                        print(fields[i][j].get_figure())
                        if fields[i][j].get_figure() is not None:
                            return False
                else:
                    if fields[i][y].get_figure() is not None:
                        return False
        elif self.start_x < x:
            for i in range(self.start_x, x):
                if self.start_y > y:
                    for j in range(y, self.start_y):
                        print(fields[i][j].get_figure())
                        if fields[i][j].get_figure() is not None:
                            return False
                elif self.start_y < y:
                    for j in range(self.start_y, y):
                        print(fields[i][j].get_figure())
                        if fields[i][j].get_figure() is not None:
                            return False
                else:
                    if fields[i][y].get_figure() is not None:
                        return False
        else:
            if self.start_y > y:
                for j in range(y, self.start_y):
                    print(fields[x][j].get_figure())
                    if fields[x][j].get_figure() is not None:
                        return False
            elif self.start_y < y:
                for j in range(self.start_y, y):
                    print(fields[x][j].get_figure())
                    if fields[x][j].get_figure() is not None:
                        return False
            else:
                if fields[x][y].get_figure() is not None:
                    return False

        _delta_x = abs(self.start_x - x)
        _delta_y = abs(self.start_y - y)

        if (_delta_x == 0 and _delta_y != 0) or (_delta_x != 0 and _delta_y == 0):
            return True
        return False
