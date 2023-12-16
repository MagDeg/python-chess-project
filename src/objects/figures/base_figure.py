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

    def draw_killed(self, surface, count_figures):
        screen = ScreenSize()

        x = count_figures % 4
        y = (count_figures - x) / 4

        y_length = screen.get_surface_size()
        x_length_start = screen.get_surface_size()

        single_field_length = int((y_length / 2) / 4)
        single_field_width = 100 / 1.5

        if self.color == Color.WHITE:
            surface.blit(pygame.transform.scale(self.img, (single_field_width, single_field_width)),
                         (x * single_field_width + x_length_start, y * single_field_width))
        else:
            surface.blit(pygame.transform.scale(self.img, (single_field_width, single_field_width)),
                         (x * single_field_width + x_length_start, y * single_field_width + int(y_length / 2)))
