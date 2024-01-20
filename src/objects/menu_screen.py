import pygame
from functions.get_screen_size import *


class MenuScreen:
    # class to draw credit screen

    def __init__(self, surface, chessboard, credit_screen):
        # getting screen size from class
        self.screensize = ScreenSize()
        # passing surface to draw on
        self.surface = surface

        # passing chessboard object
        self.chessboard = chessboard
        # passing credit screen
        self.credit_screen = credit_screen

        # variable to get current state of this screen
        self.active = False

        # variables for coordinates of credit button
        self.credits_button_x_pos = (6.5 * self.screensize.get_single_field_size())
        self.credits_button_y_pos = (7.33 * self.screensize.get_single_field_size())
        self.credits_button_x_size = self.screensize.get_single_field_size()
        self.credits_button_y_size = (0.5 * self.screensize.get_single_field_size())

        # variables for coordinates of start button
        self.start_button_x_size = (2 * self.screensize.get_single_field_size())
        self.start_button_y_size = self.screensize.get_single_field_size()
        self.start_button_x_pos = (3 * self.screensize.get_single_field_size())
        self.start_button_y_pos = (4 * self.screensize.get_single_field_size())

    def draw(self):
        # actual draw function

        # first create background (like a chessboard)
        self.create_background()
        # drawing start button on background
        self.start_button()
        # drawing credits button on background
        self.credits_button()
        # setting active variable to true, because screen is active
        self.active = True

    def create_background(self):
        # function to create background

        # loading image for background
        background = pygame.image.load('images/menu_background.png')
        # scaling background to screen size
        full_background = pygame.transform.scale(background, (self.screensize.get_surface_size(), self.screensize.get_surface_size()))
        # drawing background screen
        self.surface.blit(full_background, (0, 0))

    def start_button(self):
        # function to create start button

        # loading image for button
        start_button = pygame.image.load('images/start_button.png')
        # scaling button to required size
        sized_start_button = pygame.transform.scale(start_button, (self.start_button_x_size, self.start_button_y_size))
        # drawing button to background
        self.surface.blit(sized_start_button, (self.start_button_x_pos, self.start_button_y_pos))

    def credits_button(self):
        # function to create credits button

        # loading image for button
        credits_button = pygame.image.load('images/credits_button.png')
        # scaling button to required size
        sized_credits_button = pygame.transform.scale(credits_button, (self.credits_button_x_size, self.credits_button_y_size))
        # drawing button to background
        self.surface.blit(sized_credits_button, (self.credits_button_x_pos, self.credits_button_y_pos))

    def mouse_clicked(self, mouse_pos):
        # handler for mouse click event

        # getting mouse position from list
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]

        # if mouse click is between coordinates of button -> handle as button clicked
        if self.start_button_x_pos <= x_pos <= (self.start_button_x_pos + self.start_button_x_size) and self.start_button_y_pos <= y_pos <= (self.start_button_y_pos + self.start_button_y_size):
            # setting figures on fields
            self.chessboard.place_figures()
            # drawing chessboard with figures
            self.chessboard.draw()
            # setting active variable to false, because screen is no longer active
            self.active = False

        # if mouse click is between coordinates of button -> handle as button clicked
        if self.credits_button_x_pos <= x_pos <= (self.credits_button_x_pos + self.credits_button_x_size) and self.credits_button_y_pos <= y_pos <= (self.credits_button_y_pos + self.credits_button_y_size):
            # drawing credit screen
            self.credit_screen.draw()
            # setting active variable to false, because screen is no longer active
            self.active = False