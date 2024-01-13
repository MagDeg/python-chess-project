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
        for column in self.fields:
            for row in column:
                row.draw(self.surface)

    def check_mouse_position(self, _mouse_pos):
        # function to evaluate the position of the mouse on the field
        # turning real coordinates into field-coordinates

        # checks every field on the chessboard
        for x in self.fields:
            for y in x:
                # getting range of real coordinates of field by multiplying field coordinates with width of Singelfield
                x_start = y.x * y.w
                y_start = y.y * y.h
                x_end = x_start + y.w
                y_end = y_start + y.h

                # extracting single mouse coordinates
                mouse_x = _mouse_pos[0]
                mouse_y = _mouse_pos[1]

                # checking if mouse coordinate is in range of field
                # if true, returning the field coordinates
                if x_start <= mouse_x <= x_end:
                    if y_start <= mouse_y <= y_end:
                        return y.x, y.y

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
        field = self.fields[field_cord[0]][field_cord[1]]

        # if there is no previously selected field
        if self.field_selected is None:
            # if there is no figure on that field return, because in order to make a move you have to select a figure
            if field.get_figure() is None:
                return

            # if you already have made a move, return -> you can not make two moves on after the other
            if self.previous_side_color is field.figure.color:
                return
            else:
                # if not you make a move, so you can make the next
                self.previous_side_color = field.figure.color

            # selecting the field with the figure on it
            self.field_selected = field
            # setting color of that field to hover_color to raise it from the other
            field.set_hover_color()
            # after that the field has to redrawn to update the appearance
            field.draw(self.surface)
            # end of function
            return

        # if the same field was selected as previous it is handled as a "cancel-event"
        if self.field_selected == field:
            # resetting selected field
            self.field_selected = None
            # removing hover_color
            field.remove_hover_color()
            # redrawing to update the appearance
            field.draw(self.surface)

            # depending on the clicked figure, update previous color, to make sure to allow the player a valid move
            if field.figure.color == Color.WHITE:
                self.previous_side_color = Color.BLACK
            else:
                self.previous_side_color = Color.WHITE
            return

        # if a new field was selected, getting figure from previous selected field
        figure_selected = self.field_selected.get_figure()
        # getting figure from target field
        figure_target = field.get_figure()

        # if there is a figure from the same color on that field return because it is not a valid move
        if figure_target is not None and figure_target.color == figure_selected.color:
            return

        # check if figure is allowed to move there
        if not figure_selected.check_movement_allowance(field, self.fields):
            return

        # if there is a figure on the target
        if figure_target is not None:
            # putting figure of target field to killed figures
            self.killed_figures.append(field.get_figure())

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
        field.set_figure(figure_selected)
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
            if field.y == 7 or field.y == 0:
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
                    figure = Queen(color_selected, field.x, field.y)
                    self.count_of_later_added_figures += self.count_of_later_added_figures

                # setting new figure on the field
                field.set_figure(figure)

        # clearing the previous selected field
        self.field_selected = None
        # updating whole chessboard by redrawing
        self.draw()

    def place_figure(self):
        # place every figure on start position

        # black figures
        # pawns
        for i in range(0, 8):
            self.fields[i][1].set_figure(Pawn(Color.WHITE, i, 1))

        # rooks
        self.fields[0][0].set_figure(Rook(Color.WHITE, 0, 0))
        self.fields[7][0].set_figure(Rook(Color.WHITE, 7, 0))

        # bishops
        self.fields[2][0].set_figure(Bishop(Color.WHITE, 2, 0))
        self.fields[5][0].set_figure(Bishop(Color.WHITE, 5, 0))

        # knights
        self.fields[1][0].set_figure(Knight(Color.WHITE, 1, 0))
        self.fields[6][0].set_figure(Knight(Color.WHITE, 6, 0))

        # queen
        self.fields[3][0].set_figure(Queen(Color.WHITE, 3, 0))

        # king
        self.fields[4][0].set_figure(King(Color.WHITE, 4, 0))

        # white figures
        # pawns
        for i in range(0, 8):
            self.fields[i][6].set_figure(Pawn(Color.BLACK, i, 6))

        # rooks
        self.fields[0][7].set_figure(Rook(Color.BLACK, 0, 7))
        self.fields[7][7].set_figure(Rook(Color.BLACK, 7, 7))

        # bishops
        self.fields[2][7].set_figure(Bishop(Color.BLACK, 2, 7))
        self.fields[5][7].set_figure(Bishop(Color.BLACK, 5, 7))

        # knights
        self.fields[1][7].set_figure(Knight(Color.BLACK, 1, 7))
        self.fields[6][7].set_figure(Knight(Color.BLACK, 6, 7))

        # queen
        self.fields[3][7].set_figure(Queen(Color.BLACK, 3, 7))

        # king
        self.fields[4][7].set_figure(King(Color.BLACK, 4, 7))

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
