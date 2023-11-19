import pygame
from objects.chessboard import Chessboard

active = True

surface = pygame.display.set_mode((2560/2, 1440/2))

chessboard = Chessboard(surface)
# chessboard.build_board(80,80)

# rect = pygame.Rect((8, 8, 8, 8))
# pygame.draw.rect(surface, "red", rect)

chessboard.draw(surface)

while active:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    pygame.display.update()

pygame.quit()
