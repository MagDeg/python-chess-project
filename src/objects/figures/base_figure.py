from functions.color import *
from functions.get_screen_size import *
from functions.draw import *


class BaseFigure:
    def __init__(self, color, start_x, start_y):
        # color of figure, means black or white, ColorObject of class functions.color
        self.color = color
        # saving position, on which figure stands at the moment of selection
        self.start_x = start_x
        self.start_y = start_y
        # variable to check if figure has been moved -> essential in combination with pawn or king
        self.moved = False
        # variable for image, which will be loaded in ChildClass
        self.img = None

    def draw(self, x, y, surface, size):
        # draw figure on defined surface

        # size = size of single field
        # x,y field coordinates

        # will be overwritten in some figures for additional options

        # refreshing current position of figure
        self.start_x = x
        self.start_y = y

        # actual draw method
        # images needs to be resized on size of single field
        surface.blit(pygame.transform.scale(self.img, (size, size)), (x * size, y * size))

    def check_field_for_enemy(self, field):
        # detect if there is an enemy on the targeted field

        # if there is a figure on field check if it is an enemy or not by checking if figure is same color as self
        if field.figure is not None:
            if field.figure.color == self.color:
                return False
            return True
        return False

    def draw_killed(self, surface, count_figures):
        # function to draw figure if it has been killed by the enemy, it will be shown on the right side of the field
        # as smaller replicates

        # initialize Screensize class in order to get the size of the single fields
        screen = ScreenSize()

        # implementing new coordinate system for figures, that have been killed

        # figures will be lined in 4*y grids, so the modulo operator gets the position of the figure
        x = count_figures % 4
        # getting y coordinate of figure by dividing by the width of grid
        y = (count_figures - x) / 4

        # getting surface size of shown window from screensize class
        y_length = screen.get_surface_size()
        x_length_start = screen.get_surface_size()

        # getting width of the sections of the grid
        # surface_size * 0.30 is the size that has been added on the right side of the window, divided by 4 for the
        # columns of the grid
        single_field_width = screen.get_surface_size() * 0.30 / 4

        # if figure is from color white, it will be placed on the bottom of the window
        if self.color == Color.WHITE:
            # before drawing image it has to be resized to fit in the grid
            surface.blit(pygame.transform.scale(self.img, (single_field_width, single_field_width)),
                         (x * single_field_width + x_length_start, y * single_field_width))
        # if figure is from color black, it will be placed at the top of the window
        else:
            surface.blit(pygame.transform.scale(self.img, (single_field_width, single_field_width)),
                         (x * single_field_width + x_length_start, y_length - (y+1) * single_field_width))

    def is_figure_on_line_straight(self, target_field, fields):
        # function to detect of there is a figure between the target field and the current field, to prevent
        # overstepping

        # defining variables for coordinates of the target field
        target_x = target_field.x
        target_y = target_field.y
        # adding variable to prevent self check, so that figure won't see itself as an obstacle or the targeted enemy
        prevent_self_check = 0

        # checking if there is an enemy on the target field, to set variable on one, to represent, that it is not an
        # obstacle
        if self.check_field_for_enemy(target_field) is True:
            prevent_self_check = 1

        # if target_x is bigger that start_x the destination is on the right side of the figure
        # fields will be searched from the smallest to the highest
        if target_x > self.start_x:
            start_x = self.start_x
            end_x = target_x - prevent_self_check
        # otherwise the target is on the right side of the figure and the fields will be searched from
        # the target to the player
        else:
            start_x = target_x + prevent_self_check
            end_x = self.start_x
        # in each case by subtracting or adding the variable preventing_self_check, the figures on the end/start of
        # the line won't be viewed

        # if target_y is bigger that start_y the destination is "under" the figure
        # fields will be searched from the smallest to the highest
        if target_y > self.start_y:
            start_y = self.start_y
            end_y = target_y - prevent_self_check
        # otherwise the target is below the figure and the fields will be searched from
        # the target to the player
        else:
            start_y = target_y + prevent_self_check
            end_y = self.start_y
        # in each case by subtracting or adding the variable preventing_self_check, the figures on the end/start of
        # the line won't be viewed

        # if target_y is equal to start_y, just the x-axis has to be searched
        if target_y == self.start_y:
            for i in range(start_x, end_x):
                # make exception so that the figure on the start of the line won't be marked as an enemy
                if i != self.start_x:
                    # search the field on the coordinate and if there is a figure return True
                    if fields[i][target_y].get_figure() is not None:
                        return True
            # otherwise return false
            return False

        # if target_x is equal to start_x, just the y-axis has to be searched
        if target_x == self.start_x:
            for i in range(start_y, end_y):
                # make exception so that the figure on the start of the line won't be marked as an enemy
                if i != self.start_y:
                    # search the field on the coordinate and if there is a figure return True
                    if fields[target_x][i].get_figure() is not None:
                        return True
            # otherwise return false
            return False

    def is_figure_on_line_diagonal(self, target_field, fields):
        # function to detect of there is a figure between the target field and the current field, to prevent
        # overstepping

        # defining variables for coordinates of the target field
        target_x = target_field.x
        target_y = target_field.y

        # adding variable to prevent self check, so that figure won't see itself as an obstacle or the targeted enemy
        prevent_target_check = 0

        # it's enough to just work with the delta of the x position, because in order to
        # walk diagonal they have to be equal
        delta = abs(self.start_x - target_x)

        # checking if there is an enemy on the target field, to set variable on one, to represent, that it is not an
        # obstacle
        if self.check_field_for_enemy(target_field) is True:
            prevent_target_check = 1

        # to make a movement the delta has to be at least one
        for i in range(1, delta - prevent_target_check):
            # saving variable value, to change it later
            j = i
            # if target is on the left side the value has to be negated
            if self.start_x < target_x:
                i = i*-1
            # if target is below the value has to be negated
            if self.start_y < target_y:
                j = j*-1

            # searching the field if there is a figure
            if fields[target_x + i][target_y + j].get_figure() is not None:
                return True
        return False


