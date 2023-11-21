class Pawn:
    def __init__(self, _color, start_x, start_y):
        self.color = _color
        self.start_x = start_x
        self.start_y = start_y
    def movementType(self,_x,_y, startmode_pawn):
        _delta_x = (self.start_x) - _x
        _delta_y = (self.start_y) - _y
        if startmode_pawn == True:
            if (self.color == "Black") and  _delta_y == (1 or 2) and _delta_x == 0: #so ungefähr
                return True
            if (self.color == "White") and (self.start_y) - _y == (-1 or -2) and (self.start_x) == _x:
                return True
        else:
            if (self.color == "Black") and (self.start_y) - _y == 1 and (self.start_x) == _x:
                return True
            if (self.color == "White") and (self.start_y) - _y == -1 and (self.start_x) == _x:
                return True
        return False




bauer1 = Pawn("black")
bauer1.color
bauer2 = Pawn("weiß")
bauer2.movementType()
