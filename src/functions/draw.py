import pygame


class PygameLocal:
    def __init__(self, surface):
        self.surface = surface
    def drawRect(self, color, left, top, width, height):
        pygame.draw.rect(self.surface, color, pygame.Rect(left, top, width, height))
