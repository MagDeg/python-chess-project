from win32api import GetSystemMetrics


class ScreenSize:
    def __init__(self):
        self.surface_size = self.get_surface_size()
        pass

    def get_surface_size(self):
        height = GetSystemMetrics(1)
        width = GetSystemMetrics(0)

        if height >= width:
            self.surface_size = width * 0.90
            return self.surface_size
        else:
            self.surface_size = height * 0.90
            return self.surface_size

    def get_single_field_size(self):
        return self.surface_size/8
