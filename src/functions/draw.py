import pygame


class PygameLocal:
    # just to make the complex pygame draw method easier to use in code

    def __init__(self, surface):
        # initialising local surface variable, by passing surface as parameter
        # so actual draw method becomes easier and smaller
        self.surface = surface

    def draw_rect(self, color, left, top, width, height):
        # just calling standard pygame.draw.rect method and passing required parameters
        pygame.draw.rect(self.surface, color, pygame.Rect(left, top, width, height))
