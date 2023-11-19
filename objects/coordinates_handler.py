from objects.singlefield import SingleField


class CoordinatesHandler:

    field_coordinates = [
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
        [SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0), SingleField(0, 0)],
    ]

    def get_coordinates(self, y_axis, x_axis):
        return self.field_coordinates[y_axis][x_axis]
