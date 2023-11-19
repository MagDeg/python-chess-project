from objects.coordinates import Coordinates


class CoordinatesHandler:

    field_coordinates = {
        "A": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
        "B": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
        "C": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
        "D": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
        "E": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
        "F": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
        "G": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
        "H": [Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0), Coordinates(0, 0)],
    }

    def get_coordinates(self, y_axis, x_axis):
        return self.field_coordinates[y_axis][x_axis]
