class Queen:
    def __init__(self, _color, start_x, start_y):
        self.color = _color
        self.start_x = start_x
        self.start_y = start_y
    def movementAllowed(self,_x,_y):
        _delta_x = abs(self.start_x - _x)
        _delta_y = abs(self.start_y - _y)
        if (_delta_x == _delta_y != 0) or (_delta_x == 0 and _delta_y != 0) or (_delta_x != 0 and _delta_y == 0):
            return True
        return False