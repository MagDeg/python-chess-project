class BaseFigure:
    def __init__(self, _color, start_x, start_y):
        self.color = _color
        self.start_x = start_x
        self.start_y = start_y
        self.moved = False
