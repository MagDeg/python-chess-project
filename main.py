import pygame

surface = pygame.display.set_mode((800, 800))
rect = pygame.Rect((8, 8, 8, 8))

active = True

pygame.draw.rect(surface, "red", rect)

while active:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    pygame.display.update()

pygame.quit()
