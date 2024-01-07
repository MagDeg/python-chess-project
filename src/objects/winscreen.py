import pygame
from functions.get_screen_size import *
from functions.color import *


class WinScreen:
    def __init__(self):
        self.active = False

    def draw(self, dead_color, surface):
        if dead_color == Color.BLACK:
            self.white_winner(surface)
        if dead_color == Color.WHITE:
            self.black_winner(surface)
        self.active = True

    def black_winner(self, surface):
        screensize = ScreenSize()
        black_win_screen = pygame.image.load('images/winning_screen_black.png')
        full_black_win_screen = pygame.transform.scale(black_win_screen, (screensize.get_surface_size(), screensize.get_surface_size()))
        surface.blit(full_black_win_screen, (0, 0))

    def white_winner(self, surface):
        screensize = ScreenSize()
        white_win_screen = pygame.image.load('images/winning_screen_white.png')
        full_white_win_screen = pygame.transform.scale(white_win_screen, (screensize.get_surface_size(), screensize.get_surface_size()))
        surface.blit(full_white_win_screen, (0, 0))
