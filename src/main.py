import pygame
from functions.get_screen_size import ScreenSize
from objects.chessboard import Chessboard
from objects.credit_screen import CreditScreen
from objects.win_screen import WinScreen
from objects.menu_screen import MenuScreen


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
    menu = MenuScreen(surface, chessboard, credit_screen)

    # showing menu screen
    menu.draw()

    # prevents display from closing if code finished
    while running:

        # reloads display every time loop is called
        pygame.display.update()

        # checks if one king has been killed and calling the win_screen
        if chessboard.has_game_ended() is not False:
            win_screen.draw(chessboard.has_game_ended(), surface)

        # searching all running events
        for event in pygame.event.get():
            # if mouse pressed event recognised (mouse button click)
            if event.type == pygame.MOUSEBUTTONUP:

                # pass mouse position to chessboard class to evaluate position
                chessboard.on_select(pygame.mouse.get_pos())

                # restart program if mouse is clicked and a player won
                if win_screen.active is True:
                    main()

                # restart program if mouse is clicked and credit_screen is shown
                if credit_screen.active is True:
                    main()

                # if the button is clicked and the menu_screen is active pass mouse position to menu class for
                # evaluation
                if menu.active is True:
                    menu.mouse_clicked(pygame.mouse.get_pos())

            # if exit event recognised (pressing exit button) leaving loop
            if event.type == pygame.QUIT:
                running = False

    # closing window
    pygame.quit()


main()
