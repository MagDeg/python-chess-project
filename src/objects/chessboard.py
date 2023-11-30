from objects.singlefield import *


class Chessboard:
    def __init__(self, _surface):
        self.surface = _surface
        self.field_selected = None

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

    def add_figure_to_field(self, x, y, figure):
        self.fields[x][y].set_figure(figure)

    def on_select(self, mouse_pos):

        field_cord = self.check_mouse_position(mouse_pos)
        field = self.fields[field_cord[0]][field_cord[1]]

        if self.field_selected is None:
            if field.get_figure() is None:
                return
            self.field_selected = field
            #field.set_hover_color()
            #field.draw(self.surface)
            return
        if self.field_selected == field:
            self.field_selected = None
            #field.remove_hover_color()
            #field.draw(self.surface)
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
            pass

        field.set_figure(figure_selected)
        self.field_selected.set_figure(None)
        #self.field_selected.remove_hover_color()
        self.field_selected = None
        self.draw(self.surface)
