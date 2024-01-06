import time

import pygame
from functions.get_screen_size import *
from objects.chessboard import Chessboard


from pygame.locals import*


class Menu:
    def __init__(self, surface, chessboard, credit_screen):
        self.screensize = ScreenSize()
        self.surface = surface

        self.chessboard = chessboard
        self.credit_screen = credit_screen

        self.active = False

        self.credits_button_x_pos = (6.5 * self.screensize.get_single_field_size())
        self.credits_button_y_pos = (7.33 * self.screensize.get_single_field_size())
        self.credits_button_x_size = self.screensize.get_single_field_size()
        self.credits_button_y_size = (0.5 * self.screensize.get_single_field_size())

        self.start_button_x_size = (2 * self.screensize.get_single_field_size())
        self.start_button_y_size = self.screensize.get_single_field_size()
        self.start_button_x_pos = (3 * self.screensize.get_single_field_size())
        self.start_button_y_pos = (4 * self.screensize.get_single_field_size())

    def draw(self):
        self.create_background()
        self.start_button()
        self.credits_button()
        self.active = True

    def create_background(self):
        background = pygame.image.load('images/menu_background.png')
        full_background = pygame.transform.scale(background, (self.screensize.get_surface_size(), self.screensize.get_surface_size()))
        self.surface.blit(full_background, (0, 0))

    def start_button(self):

        start_button = pygame.image.load('images/start_button.png')
        sized_start_button = pygame.transform.scale(start_button, (self.start_button_x_size, self.start_button_y_size))
        self.surface.blit(sized_start_button, (self.start_button_x_pos, self.start_button_y_pos))

    def credits_button(self):

        credits_button = pygame.image.load('images/credits_button.png')
        sized_credits_button = pygame.transform.scale(credits_button, (self.credits_button_x_size, self.credits_button_y_size))
        self.surface.blit(sized_credits_button, (self.credits_button_x_pos, self.credits_button_y_pos))

    def mouse_clicked(self, mouse_pos):
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]

        if self.start_button_x_pos <= x_pos <= (self.start_button_x_pos + self.start_button_x_size) and self.start_button_y_pos <= y_pos <= (self.start_button_y_pos + self.start_button_y_size):
            # setting figures on fields
            self.chessboard.place_figure()
            # drawing chessboard with figures
            self.chessboard.draw()
            self.active = False

        if self.credits_button_x_pos <= x_pos <= (self.credits_button_x_pos + self.credits_button_x_size) and self.credits_button_y_pos <= y_pos <= (self.credits_button_y_pos + self.credits_button_y_size):
            self.credit_screen.draw()
            self.active = False



