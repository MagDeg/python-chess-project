from objects.field import Field


class CoordinatesHandler:

    field_coordinates = [
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
        [Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0), Field(0, 0)],
    ]

    def get_coordinates(self, y_axis, x_axis):
        return self.field_coordinates[y_axis][x_axis]
