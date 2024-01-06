import pygame
from functions.get_screen_size import ScreenSize


class CreditScreen:
    def __init__(self, surface):
        self.active = False
        self.surface = surface

    def draw(self):
        screensize = ScreenSize()
        credits_screen = pygame.image.load('images/credits_screen.PNG')
        full_credits_screen = pygame.transform.scale(credits_screen, (screensize.get_surface_size(), screensize.get_surface_size()))
        self.surface.blit(full_credits_screen, (0, 0))
        self.active = True
