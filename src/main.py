import pygame
from functions.get_screen_size import ScreenSize
from objects.chessboard import Chessboard

# variable for status of program
running = True

# initialising class for screen size getter
screen_size = ScreenSize()
# defining size of shown screen with scaled screen size (got from screen size class)
surface = pygame.display.set_mode((screen_size.surface_size + screen_size.surface_size * 0.30, screen_size.surface_size))

# initialising pygame
pygame.init()
# initialising chessboard class with surface to draw on
chessboard = Chessboard(surface)

# setting figures on fields
chessboard.place_figure()

# drawing chessboard with figures
chessboard.draw(surface)

# prevents display from closing if code finished
while running:

    # reloads display every time loop is called
    pygame.display.update()

    if chessboard.is_king_dead():
        # running = False
        #TODO: IMPLEMENT VICTORY SCREEN
        pass

    # searching all running events
    for event in pygame.event.get():
        # if mouse pressed event recognised (mouse button click)
        if event.type == pygame.MOUSEBUTTONUP:
            # pass mouse position to chessboard class to evaluate position
            chessboard.on_select(pygame.mouse.get_pos())

        # if exit event recognised (pressing exit button) leaving loop
        if event.type == pygame.QUIT:
            running = False

# closing window
pygame.quit()
