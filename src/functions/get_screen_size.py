from win32api import GetSystemMetrics


class ScreenSize:
    def __init__(self):
        # initializing class variable for surface size for later using in program code
        self.surface_size = self.get_surface_size()

    def get_surface_size(self):
        # getting width and height of device screen
        height = GetSystemMetrics(1)
        width = GetSystemMetrics(0)

        # the chessboard is a square, to get the largest possible size, the smallest size has to be
        # considered to get the maximum length
        if height >= width:
            # multiplying the smallest size with factor to make the window a little bit smaller
            self.surface_size = width * 0.90
            return self.surface_size
        else:
            # multiplying the smallest size with factor to make the window a little bit smaller
            self.surface_size = height * 0.90
            return self.surface_size

    def get_single_field_size(self):
        # a chessboard has 64 fields in a 8x8 grid, so the width is 1/8 of the total width
        # because it is a square the width is also the height, so it is enough to work with just one value
        return self.surface_size/8
