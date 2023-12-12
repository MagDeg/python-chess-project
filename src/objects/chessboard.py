from objects.figures.bishop import Bishop
from objects.figures.king import King
from objects.figures.knight import Knight
from objects.figures.pawn import Pawn
from objects.figures.queen import Queen
from objects.figures.rook import Rook
from objects.singlefield import SingleField
from functions.color import Color


class Chessboard:
    def __init__(self, surface):
        self.surface = surface
        self.field_selected = None

        self.killed_figures = []
        self.fields = []

        for x in range(0, 8):
            column = []
            for y in range(0, 8):
                column.append(SingleField(x, y))

            self.fields.append(column)

    def draw(self, surface):
        for column in self.fields:
            for row in column:
                row.draw(surface)

    def check_mouse_position(self, _mouse_pos):
        for x in self.fields:
            for y in x:
                x_start = y.x * y.w
                y_start = y.y * y.h
                x_end = x_start + y.w
                y_end = y_start + y.h

                mouse_x = _mouse_pos[0]
                mouse_y = _mouse_pos[1]

                if x_start <= mouse_x <= x_end:
                    if y_start <= mouse_y <= y_end:
                        return y.x, y.y

        return 0, 0

    def add_figure_to_field(self, x, y, figure):
        self.fields[x][y].set_figure(figure)

    def on_select(self, mouse_pos):

        field_cord = self.check_mouse_position(mouse_pos)
        field = self.fields[field_cord[0]][field_cord[1]]

        if self.field_selected is None:
            if field.get_figure() is None:
                return
            self.field_selected = field
            field.set_hover_color()
            field.draw(self.surface)
            return
        if self.field_selected == field:
            self.field_selected = None
            field.remove_hover_color()
            field.draw(self.surface)
            return

        figure_selected = self.field_selected.get_figure()
        figure_target = field.get_figure()

        if figure_target is not None and figure_target.color == figure_selected.color:
            return

        # check if figure is allowed to move there
        if not figure_selected.check_movement_allowance(field):
            return

        if figure_target is not None:
            # enemy on field
            # TODO: implement enemy kill
            self.killed_figures.append(field.get_figure())

            count_white_figures = 0
            count_black_figures = 0

            for i in self.killed_figures:
                if i.color == Color.WHITE:
                    i.draw_killed(self.surface, count_white_figures)
                    count_white_figures += 1
                else:
                    i.draw_killed(self.surface, count_black_figures)
                    count_black_figures += 1


        field.set_figure(figure_selected)
        self.field_selected.set_figure(None)
        self.field_selected.remove_hover_color()
        self.field_selected = None
        self.draw(self.surface)



    def place_figure(self):
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

    def is_king_dead(self):
        for i in self.killed_figures:
            if type(i) is King:
                print("King is dead")
                return True

