import pygame


class PygameUtils:
    # just to make the complex pygame draw method easier to use in code

    @staticmethod
    def draw_rect(color, left, top, width, height, surface):
        # just calling standard pygame.draw.rect method and passing required parameters
        pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))


