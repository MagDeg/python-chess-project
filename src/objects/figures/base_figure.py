import pygame
from functions.color import *
from functions.get_screen_size import *
from functions.draw import *


class BaseFigure:
    def __init__(self, color, start_x, start_y):
        self.color = color
        self.start_x = start_x
        self.start_y = start_y
        self.moved = False
        self.img = None

    def draw(self, x, y, surface, size):
        self.start_x = x
        self.start_y = y
        surface.blit(pygame.transform.scale(self.img, (size, size)), (x * size, y * size))

    def check_field_for_enemy(self, field):
        if field.figure is not None:
            if field.figure.color == self.color:
                return False
            return True
        return False

    def draw_killed(self, surface, count_figures):
        screen = ScreenSize()

        x = count_figures % 4
        y = (count_figures - x) / 4

        y_length = screen.get_surface_size()
        x_length_start = screen.get_surface_size()

        single_field_width = screen.get_surface_size() * 0.30 / 4

        if self.color == Color.WHITE:
            surface.blit(pygame.transform.scale(self.img, (single_field_width, single_field_width)),
                         (x * single_field_width + x_length_start, y * single_field_width))
        else:
            surface.blit(pygame.transform.scale(self.img, (single_field_width, single_field_width)),
                         (x * single_field_width + x_length_start, y_length - (y+1) * single_field_width))

    def is_figure_on_line_straight(self, target_field, fields):
        target_x = target_field.x
        target_y = target_field.y
        prevent_self_check = 0

        if self.check_field_for_enemy(target_field) is True:
            prevent_self_check = 1

        if target_x > self.start_x:
            start_x = self.start_x
            end_x = target_x - prevent_self_check
        else:
            start_x = target_x + prevent_self_check
            end_x = self.start_x
        if target_y > self.start_y:
            start_y = self.start_y
            end_y = target_y - prevent_self_check
        else:
            start_y = target_y + prevent_self_check
            end_y = self.start_y

        if target_y == self.start_y:
            for i in range(start_x, end_x):
                if i != self.start_x:
                    if fields[i][target_y].get_figure() is not None:
                        return True
            return False

        if target_x == self.start_x:
            for i in range(start_y, end_y):
                if i != self.start_y:
                    if fields[target_x][i].get_figure() is not None:
                        return True
            return False

        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                if fields[i][j].get_figure() is not None:
                    return True
            return False

    def is_figure_on_line_diagonal(self, target_field, fields):
        target_x = target_field.x
        target_y = target_field.y

        prevent_target_check = 0

        # it's enough to just work with the delta of the x position, because in order to
        # walk diagonal they have to be equal
        delta = abs(self.start_x - target_x)

        if self.check_field_for_enemy(target_field) is True:
            prevent_target_check = 1

        for i in range(1, delta - prevent_target_check):
            j = i
            if self.start_x < target_x:
                i = i*-1
            if self.start_y < target_y:
                j = j*-1

            if fields[target_x + i][target_y + j].get_figure() is not None:
                print(True)
                return True
        return False


