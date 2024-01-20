import pygame
from functions.get_screen_size import ScreenSize


class CreditScreen:
    # class to draw credit screen

    def __init__(self, surface):
        # variable to get current state of this screen
        self.active = False
        # surface to draw on
        self.surface = surface

    def draw(self):
        # actual draw function

        # getting screen size from class
        screensize = ScreenSize()
        # loading image for credit screen
        credits_screen = pygame.image.load('images/credits_screen.PNG')
        # scaling image to the correct size of the screen
        full_credits_screen = pygame.transform.scale(credits_screen, (screensize.get_surface_size(), screensize.get_surface_size()))
        # drawing image on screen
        self.surface.blit(full_credits_screen, (0, 0))
        # setting active variable to true, because screen is active
        self.active = True
