import pygame
from functions.get_screen_size import ScreenSize
from objects.chessboard import Chessboard
from objects.figures.pawn import Pawn


# variable to represent status of display; ture = display still running, false = display was exited
active = True
mouse_pos = 0

# initialising class for screen size getter
screen_size = ScreenSize()
# defining size of shwon screen with scaled screen size (got from screen size class)
surface = pygame.display.set_mode((screen_size.surface_size, screen_size.surface_size))

# initialising 
chessboard = Chessboard(surface)
chessboard.draw(surface)
chessboard.fields[0][0].set_figure(Pawn("black", 1, 1))
print(chessboard.fields[0][0].check_figure().color)

# prevents display from closing if code finished
while active:

    # searching all running events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            print(chessboard.check_mouse_position(mouse_pos))

        # if exit event recognised (pressing exit button) leaving loop
        if event.type == pygame.QUIT:
            active = False
    pygame.display.update()

# closing window
pygame.quit()
