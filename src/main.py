import pygame
from functions.get_screen_size import ScreenSize
from objects.chessboard import Chessboard
from objects.figures.pawn import Pawn
from functions.color import Color

running = True

# initialising class for screen size getter
screen_size = ScreenSize()
# defining size of shown screen with scaled screen size (got from screen size class)
surface = pygame.display.set_mode((screen_size.surface_size, screen_size.surface_size))

color = Color()

# initialising
pygame.init()
chessboard = Chessboard(surface)
chessboard.draw(surface)
chessboard.fields[0][0].set_figure(Pawn(color.WHITE, 0, 0))


def tempoaray_moving_method(x_pos_actual, y_pos_actual, x_pos_new, y_pos_new):
    # check if move is allowed
    if chessboard.fields[x_pos_actual][y_pos_actual].figure.check_movement_allowance(x_pos_new, y_pos_new):
        # add figure from start field to new field
        chessboard.fields[x_pos_new][y_pos_new].set_figure(chessboard.fields[x_pos_actual][y_pos_actual].figure)
        # resetting start field figure to none
        chessboard.fields[x_pos_actual][y_pos_actual].set_figure(None)
        # draw figure to new field
        chessboard.fields[x_pos_new][y_pos_new]._draw_figure(x_pos_new, y_pos_new, surface)
    else:
        print("irregular move")


field_selected = None

# prevents display from closing if code finished
while running:

    pygame.display.update()

    # searching all running events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            chessboard.on_select(pygame.mouse.get_pos())

        # if exit event recognised (pressing exit button) leaving loop
        if event.type == pygame.QUIT:
            running = False

# closing window
pygame.quit()
