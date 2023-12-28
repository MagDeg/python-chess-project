import pygame.image
from objects.figures.base_figure import BaseFigure
from functions.color import Color


class Pawn(BaseFigure):

    def __init__(self, color, start_x, start_y):
        super().__init__(color, start_x, start_y)
        if color == Color.WHITE:
            self.img = pygame.image.load("images/white_pawn.png").convert_alpha()
        else:
            self.img = pygame.image.load("images/black_pawn.png").convert_alpha()

    def check_field_for_enemy(self, field):
        if field.figure is None:
            return False
        if field.figure.color == self.color:
            return False

        return True

    def check_movement_allowance(self, field, fields):

        x = field.x
        y = field.y

        delta_x = (self.start_x - x)
        delta_y = (self.start_y - y)

        enemy_on_field = self.check_field_for_enemy(field)

        if enemy_on_field is False:

            if self.is_figure_on_line_straight(field, fields) is True:
                return False

            if (self.moved is False or self.moved is None) and (delta_x == 0):
                if (self.color == Color.BLACK and (delta_y == 1 or delta_y == 2)) or (
                        self.color == Color.WHITE and (delta_y == -1 or delta_y == -2)):
                    print("true")
                    return True
            else:
                if (self.color == Color.BLACK) and (delta_y == 1) and (delta_x == 0):
                    print("true")
                    return True
                if (self.color == Color.WHITE) and (delta_y == -1) and (delta_x == 0):
                    print("true")
                    return True
        else:
            if (delta_x == 1 or delta_x == -1) and delta_y == 1 and self.color == Color.BLACK:
                return True
            if (delta_x == -1 or delta_x == 1) and delta_y == -1 and self.color == Color.WHITE:
                return True
        print("false")
        return False

    def _change_moved(self):
        print("pre-change:" + str(self.moved))
        if self.moved is False:
            self.moved = True
            return

    def draw(self, x, y, surface, size):
        if not (self.start_x == x and self.start_y == y):
            self._change_moved()
        self.start_x = x
        self.start_y = y
        surface.blit(pygame.transform.scale(self.img, (size, size)), (x * size, y * size))

