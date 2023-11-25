from gpanel import*

class cord:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        


makeGPanel(-100,100,-100,100)

setColor("black")

addFactor = 0

repeat 4:
    setColor("black")
    fillRectangle(21 + addFactor, 21, 0 + addFactor, 0)
    addFactor = addFactor + 21
    setColor("white")
    fillRectangle(21 + addFactor, 21, 0 + addFactor, 0)
    addFactor = addFactor + 21


cords = {
    "A" : [cord(0,0), cord(10,10), "3;4"],
    "B" : []
}


print(cords["A"][1].x)
print(cords["A"][1].y)


