import pygame
from functions.get_screen_size import ScreenSize
from objects.chessboard import Chessboard
from objects.figures.bishop import Bishop
from objects.figures.king import King
from objects.figures.knight import Knight
from objects.figures.pawn import Pawn
from functions.color import Color
from objects.figures.queen import Queen
from objects.figures.rook import Rook

running = True

# initialising class for screen size getter
screen_size = ScreenSize()
# defining size of shown screen with scaled screen size (got from screen size class)
surface = pygame.display.set_mode((screen_size.surface_size + screen_size.surface_size*0.30, screen_size.surface_size))

color = Color()


def temporary_setting_figures_method(fields):
    # black figures
    # pawns
    for i in range(0, 8):
        fields[i][1].set_figure(Pawn(color.WHITE, i, 1))

    # rooks
    fields[0][0].set_figure(Rook(color.WHITE, 0, 0))
    fields[7][0].set_figure(Rook(color.WHITE, 7, 0))

    # bishops
    fields[2][0].set_figure(Bishop(color.WHITE, 2, 0))
    fields[5][0].set_figure(Bishop(color.WHITE, 5, 0))

    # knights
    fields[1][0].set_figure(Knight(color.WHITE, 1, 0))
    fields[6][0].set_figure(Knight(color.WHITE, 6, 0))

    # queen
    fields[3][0].set_figure(Queen(color.WHITE, 3, 0))

    # king
    fields[4][0].set_figure(King(color.WHITE, 4, 0))

    # white figures
    # pawns
    for i in range(0, 8):
        fields[i][6].set_figure(Pawn(color.BLACK, i, 6))

    # rooks
    fields[0][7].set_figure(Rook(color.BLACK, 0, 7))
    fields[7][7].set_figure(Rook(color.BLACK, 7, 7))

    # bishops
    fields[2][7].set_figure(Bishop(color.BLACK, 2, 7))
    fields[5][7].set_figure(Bishop(color.BLACK, 5, 7))

    # knights
    fields[1][7].set_figure(Knight(color.BLACK, 1, 7))
    fields[6][7].set_figure(Knight(color.BLACK, 6, 7))

    # queen
    fields[3][7].set_figure(Queen(color.BLACK, 3, 7))

    # king
    fields[4][7].set_figure(King(color.BLACK, 4, 7))

# initialising
pygame.init()
chessboard = Chessboard(surface)
temporary_setting_figures_method(chessboard.fields)

chessboard.draw(surface)

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
