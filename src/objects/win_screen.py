import pygame
from functions.get_screen_size import *
from functions.color import *
from objects.figures.king import King


class WinScreen:
    # class to draw win screen

    def __init__(self):
        # variable to get current state of this screen
        self.active = False

    def draw(self, end_object, surface):
        # drawing win screen

        # if one of the kings were killed
        if type(end_object) is King:
            # calling the corresponding winning screen according to which color won
            if end_object.color == Color.BLACK:
                self.white_winner(surface)
            if end_object.color == Color.WHITE:
                self.black_winner(surface)
        else:
            # it is a draw, no king was killed
            self.draw_screen(surface)
        # setting active variable to true, because screen is active
        self.active = True

    def black_winner(self, surface):
        # getting screen size
        screensize = ScreenSize()
        # loading image of winning screen for black as winning side
        black_win_screen = pygame.image.load('images/winning_screen_black.png')
        # scaling image to screen size
        full_black_win_screen = pygame.transform.scale(black_win_screen, (screensize.get_surface_size(), screensize.get_surface_size()))
        # drawing image
        surface.blit(full_black_win_screen, (0, 0))

    def white_winner(self, surface):
        # getting screen size
        screensize = ScreenSize()
        # loading image of winning screen for white as winning side
        white_win_screen = pygame.image.load('images/winning_screen_white.png')
        # scaling image to screen size
        full_white_win_screen = pygame.transform.scale(white_win_screen, (screensize.get_surface_size(), screensize.get_surface_size()))
        # drawing image
        surface.blit(full_white_win_screen, (0, 0))

    def draw_screen(self, surface):
        # getting screen size
        screensize = ScreenSize()
        # loading image of draw screen
        draw_screen = pygame.image.load('images/draw_screen.png')
        # scaling image to screen size
        full_draw_screen = pygame.transform.scale(draw_screen, (screensize.get_surface_size(), screensize.get_surface_size()))
        # drawing image
        surface.blit(full_draw_screen, (0, 0))
