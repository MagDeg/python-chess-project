import time

import pygame
from functions.get_screen_size import ScreenSize
from objects.chessboard import Chessboard
from objects.credit_screen import CreditScreen
from objects.winscreen import WinScreen
from objects.menu import Menu


def main():
    # variable for status of program
    running = True

    # initialising class for screen size getter
    screen_size = ScreenSize()
    # defining size of shown screen with scaled screen size (got from screen size class)
    surface = pygame.display.set_mode(
        (screen_size.surface_size + screen_size.surface_size * 0.30, screen_size.surface_size))

    # initialising pygame
    pygame.init()
    # initialising chessboard class with surface to draw on
    chessboard = Chessboard(surface)

    # initialising wining class for victory
    win_screen = WinScreen()

    # initialising CreditScreen class for credits
    credit_screen = CreditScreen(surface)

    # initialising menu class for startup display
    menu = Menu(surface, chessboard, credit_screen)

    menu.draw()

    # prevents display from closing if code finished
    while running:

        # reloads display every time loop is called
        pygame.display.update()

        if chessboard.is_king_dead() is not None:
            win_screen.draw(chessboard.is_king_dead().color, surface)

        # searching all running events
        for event in pygame.event.get():
            # if mouse pressed event recognised (mouse button click)
            if event.type == pygame.MOUSEBUTTONUP:

                # pass mouse position to chessboard class to evaluate position
                chessboard.on_select(pygame.mouse.get_pos())

                if win_screen.active is True:
                    main()

                if credit_screen.active is True:
                    main()

                if menu.active is True:
                    menu.mouse_clicked(pygame.mouse.get_pos())

            # if exit event recognised (pressing exit button) leaving loop
            if event.type == pygame.QUIT:
                running = False

    # closing window
    pygame.quit()


main()
