import pygame


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