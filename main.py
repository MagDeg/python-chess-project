import pygame
from functions.get_screen_size import ScreenSize
from objects.chessboard import Chessboard

# variable to represent status of display; ture = display still running, false = display was exited
active = True

screen_size = ScreenSize()
surface = pygame.display.set_mode((screen_size.surface_size, screen_size.surface_size))

chessboard = Chessboard(surface)
chessboard.draw(surface)

# prevents display from closing if code finished
while active:

    # searching all running events
    for event in pygame.event.get():
        # if exit event recognised (pressing exit button) leaving loop
        if event.type == pygame.QUIT:
            active = False
    pygame.display.update()

# closing window
pygame.quit()
