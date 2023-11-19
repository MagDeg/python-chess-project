import pygame


class Field:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.w = 80
        self.h = 80

    def draw(self, surface):
        x1 = self.x * self.w
        y1 = self.y * self.h

        pygame.draw.rect(surface, "red", pygame.Rect(x1, y1, self.w, self.h))
