from objects.figures.bishop import Bishop
from objects.figures.king import King
from objects.figures.knight import Knight
from objects.figures.pawn import Pawn
from objects.figures.queen import Queen
from objects.figures.rook import Rook
from objects.singlefield import SingleField
from functions.color import Color
import random


class Chessboard:
    def __init__(self, surface):
        # initialising surface to draw on
        self.surface = surface

        # variable to store the selected field of the chessboard
        self.field_selected = None

        # variable to store which side (=color) made the last move
        self.previous_side_color = Color.BLACK

        # list to store all killed figures
        self.killed_figures = []

        # list to store every field on the chessboard
        self.fields = []

        # count of all figures that had been added after the game had started
        self.count_of_later_added_figures = 0

        # filling the list with the "raw" fields
        # adding for every x-box a list with all the y-boxes of this column
        for x in range(0, 8):
            # eight field wide
            column = []
            for y in range(0, 8):
                # eight fields tall
                # passing the x and y as field coordinates to the field
                column.append(SingleField(x, y))

            # adding filled column for every x to the list
            self.fields.append(column)

    def draw(self):
        # function to draw the raw chessboard

        # goes in every field class instance and calls the draw event by passing the surface to draw upon
        for row in self.fields:
            for field in row:
                field.draw(self.surface)

    def check_mouse_position(self, _mouse_pos):
        # function to evaluate the position of the mouse on the field
        # turning real coordinates into field-coordinates

        # checks every field on the chessboard
        for row in self.fields:
            for field in row:
                # getting range of real coordinates of field by multiplying field coordinates with width of Singelfield
                x_start = field.x * field.w
                y_start = field.y * field.h
                x_end = x_start + field.w
                y_end = y_start + field.h

                # extracting single mouse coordinates
                mouse_x = _mouse_pos[0]
                mouse_y = _mouse_pos[1]

                # checking if mouse coordinate is in range of field
                # if true, returning the field coordinates
                if x_start <= mouse_x <= x_end:
                    if y_start <= mouse_y <= y_end:
                        return field.x, field.y

        # if no field matches, click is outside the board and it returns the first coordinates
        return 0, 0

    def add_figure_to_field(self, x, y, figure):
        # function to add a figure to single-field, by passing the figure itself and the field-coordinate of the field
        self.fields[x][y].set_figure(figure)

    def on_select(self, mouse_pos):
        # handler for mouseclick

        # calculating field-coordinate of real coordinate
        field_cord = self.check_mouse_position(mouse_pos)
        # getting the selected field from the rest of the fields
        target_field = self.fields[field_cord[0]][field_cord[1]]

        # if there is no previously selected field
        if self.field_selected is None:
            # if there is no figure on that field return, because in order to make a move you have to select a figure
            if target_field.get_figure() is None:
                return

            # if you already have made a move, return -> you can not make two moves on after the other
            if self.previous_side_color is target_field.figure.color:
                return

            # if you do not make a move, so you can make the next
            self.previous_side_color = target_field.figure.color

            # selecting the field with the figure on it
            self.field_selected = target_field
            # setting color of that field to hover_color to raise it from the other
            target_field.set_hover_color()
            # after that the field has to redrawn to update the appearance
            target_field.draw(self.surface)
            # end of function
            return

        # if the same field was selected as previous it is handled as a "cancel-event"
        if self.field_selected == target_field:
            # resetting selected field
            self.field_selected = None
            # removing hover_color
            target_field.remove_hover_color()
            # redrawing to update the appearance
            target_field.draw(self.surface)

            # depending on the clicked figure, update previous color, to make sure to allow the player a valid move
            if target_field.figure.color == Color.WHITE:
                self.previous_side_color = Color.BLACK
            else:
                self.previous_side_color = Color.WHITE
            return

        # if a new field was selected, getting figure from previous selected field
        figure_selected = self.field_selected.get_figure()
        # getting figure from target field
        figure_target = target_field.get_figure()

        # if there is a figure from the same color on that field return because it is not a valid move
        if figure_target is not None and figure_target.color == figure_selected.color:
            return

        # check if figure is allowed to move there
        if not figure_selected.check_movement_allowance(target_field, self.fields):
            return

        # this message can only be returned by a king, which means that the castling has to happen
        if figure_selected.check_movement_allowance(target_field, self.fields) == "castling":
            # setting selected figure to the target field, because conditions were checked in king class
            target_field.set_figure(figure_selected)
            # getting position of the rook, which changes depending on the side of the king
            # can be got by comparing target-x and selected-x
            if self.field_selected.x > target_field.x:
                # if the rook is on the left side of the king it is a field more away,
                # because of the position of the queen
                field_next_to_target = self.fields[target_field.x - 2][target_field.y]
                # placing rook to a field before the king
                self.fields[self.field_selected.x - 1][self.field_selected.y].set_figure(
                    field_next_to_target.get_figure())
                # removing figure form original field
                field_next_to_target.set_figure(None)
            else:
                # if the rook is on the left side of the king it is a field more away,
                # because of the position of the queen
                field_next_to_target = self.fields[target_field.x + 1][target_field.y]
                # placing rook to a field before the king
                self.fields[self.field_selected.x + 1][self.field_selected.y].set_figure(
                    field_next_to_target.get_figure())
                # removing figure form original field
                field_next_to_target.set_figure(None)

        # if there is a figure on the target
        if figure_target is not None:
            # putting figure of target field to killed figures
            self.killed_figures.append(target_field.get_figure())

            # adding counter for figures of each color
            count_white_figures = 0
            count_black_figures = 0

            # draw every figure in the list
            for i in self.killed_figures:
                if i.color == Color.WHITE:
                    i.draw_killed(self.surface, count_white_figures)
                    count_white_figures += 1
                else:
                    i.draw_killed(self.surface, count_black_figures)
                    count_black_figures += 1

        # moving figure to target field
        target_field.set_figure(figure_selected)
        # removing figure from previous field
        self.field_selected.set_figure(None)
        # removing hover_color
        self.field_selected.remove_hover_color()

        # if the figure is a pawn, it has a special feature
        # if it is on the other side of the field it changes to another figure like a queen
        # in our case the figure can't be chosen by the player, instead it will be a random figure that was
        # already killed (except for another pawn)
        if type(figure_selected) is Pawn:
            # defining list for all figures with the same color as the selected pawn
            killed_same_color = []
            # getting the color of the selected pawn
            color_selected = figure_selected.color
            # if the pawn has reached the other end of the board
            # in this case there is no need to differentiate between white and black, because the different figure
            # in each case can not reach a position behind itself (so the black pawn can not reach position 7,
            # because it spawned on 6 and can only move towards y negative
            if target_field.y == 7 or target_field.y == 0:
                # going through every entry in list of killed figures
                for i in self.killed_figures:
                    # if there is a king found the game ends
                    if type(i) is King:
                        return
                    # put every entry that is not a pawn and has the same color as the selected pawn into the list
                    if i.color == color_selected and type(i) is not Pawn:
                        killed_same_color.append(i)

                # if the list is not empty (meaning there were other figures killed than pawns)
                if len(killed_same_color) != 0:
                    # select a random figure from the list
                    figure = random.choice(killed_same_color)
                    # remove it from the list of killed figures (so it is "revived")
                    self.killed_figures.remove(figure)
                else:
                    # if there is no entry the new figure is always a queen (so it is a new object in the game)
                    figure = Queen(color_selected, target_field.x, target_field.y)
                    self.count_of_later_added_figures += self.count_of_later_added_figures

                # setting new figure on the field
                target_field.set_figure(figure)

        # clearing the previous selected field
        self.field_selected = None
        # updating whole chessboard by redrawing
        self.draw()

    def place_figures(self):
        # place every figure on start position

        # defining map with the figure types
        figure_types = {
            "P": Pawn,
            "R": Rook,
            "B": Bishop,
            "N": Knight,
            "K": King,
            "Q": Queen,
        }

        # modelling chessboard in a 2 dimensional list
        figures = [
            ["wR", "wB", "wN", "wQ", "wK", "wN", "wB", "wR"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            [],
            [],
            [],
            [],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["bR", "bB", "bN", "bQ", "bK", "bN", "bB", "bR"],
        ]

        y = 0
        for row in figures:
            # x coordinate has to be reset after every row
            x = 0
            for figure in row:
                # setting color to white
                color = Color.WHITE

                # if the string of the figure has a "b" at the first position, it means the figure has to be black
                if figure[0] == "b":
                    # color set to black
                    color = Color.BLACK

                # getting figure type with the second character of the string and the predefined map
                figure_type = figure_types[figure[1]]

                # if there is a figure type
                if figure_type is not None:
                    # placing figure to field
                    self.fields[x][y].set_figure(figure_type(color, x, y))
                # moving position one field ahead
                x += 1
            # moving position one field ahead
            y += 1

    def has_game_ended(self):
        # function to check if the game has ended, meaning either one of the kings was killed
        # or all figures but the kings were killed

        # getting count of all killed figures
        count_of_killed_figures = len(self.killed_figures)

        # if there is an item of type King return it, either return None
        for i in self.killed_figures:
            if type(i) is King:
                return i
        # the game has originally 30 figures without the two kings, so the count of later added figures are added
        # to this number to determine if there are only two kings left, which means the game is a draw
        if count_of_killed_figures == 30 + self.count_of_later_added_figures:
            return True
        return False
