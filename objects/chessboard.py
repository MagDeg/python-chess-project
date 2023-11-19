import pygame


class Chessboard:
    def __init__(self, _surface):
        self.surface = _surface

    def build_board(self, x_axis_size, y_axis_size):
        pygame.draw.rect(self.surface, "red", pygame.Rect(80, 80, 80, 80))
