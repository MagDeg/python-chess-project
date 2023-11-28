import pygame.image
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Pawn(BaseFigure):
    def __init__(self, _color, start_x, start_y):
        super().__init__(_color, start_x, start_y)
        self.img = pygame.image.load("E:/PyDev/python-chess-project/src/images/white_pawn.png").convert()

    def check_movement_allowance(self, field):

        x = field.x
        y = field.y

        _delta_x = (self.start_x - x)
        _delta_y = (self.start_y - y)

        color = Color()

        print(_delta_x, _delta_y)

        if (self.moved == False) and (_delta_x == 0):
            if (self.color == color.BLACK and (_delta_y == 1 or _delta_y == 2)) or (
                    self.color == color.WHITE and (_delta_y == -1 or _delta_y == -2)):
                print("true")
                return True
        else:
            if (self.color == color.BLACK) and (_delta_y == 1) and (_delta_x == 0):
                print("true")
                return True
            if (self.color == color.WHITE) and (_delta_y == -1) and (_delta_x == 0):
                print("true")
                return True
        return False

    def draw(self, x, y, surface, size):

        if not self.moved:
            # not on starting position
            self.moved = True
        print("drawn")
        self.start_x = x
        self.start_y = y
        # implement draw method
        surface.blit(pygame.transform.scale(self.img, (size, size)), (x*size, y*size))
        pygame.display.flip()
