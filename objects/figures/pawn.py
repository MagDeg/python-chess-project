

class Pawn:
    def __init__(self, _color, start_x, start_y):
        self.color = _color
        self.start_x = start_x
        self.start_y = start_y
    def movementAllowed(self,_x,_y, startmode_pawn):
        _delta_x = (self.start_x - _x)
        _delta_y = (self.start_y - _y)
        if (startmode_pawn == True) and (_delta_x == 0):
            if self.color == "Black" and (_delta_y == 1 or _delta_y == 2) or (self.color == "White" and (_delta_y == -1 or _delta_y == -2)):
                return True
        else:
            if (self.color == "Black") and (_delta_y == 1):
                return True
            if (self.color == "White") and (_delta_y == -1):
                return True
        return False



pawn = Pawn("White", 2, 2)
var = pawn.movementType(2,3,True)
print(var)
