class Rover:
    def __init__(self, x, y, orientation, mapx, mapy):
        self.x = int(x)
        self.y = int(y)
        self.orientation = orientation
        self.mapx = int(mapx)
        self.mapy = int(mapy)

    def move(self, text):
        for x in text:
            if x in "LR":
                self.turn(x)
            else:
                self.forward()
            if self.outOfBounds():
                return self.printOutput(True)
        return self.printOutput()

    def turn(self, direction):
        directions = "NESW"
        turnValues = {"L": -1, "R": 1}
        currentDirectionIndex = directions.index(self.orientation)
        turnIndex = currentDirectionIndex + turnValues[direction]
        if turnIndex >= len(directions):
            turnIndex = 0
        self.orientation = directions[turnIndex]

    def forward(self):
        orientationMove = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}
        movement = orientationMove[self.orientation]
        self.x += movement[0]
        self.y += movement[1]

    def outOfBounds(self):
        if self.x > self.mapx or self.y > self.mapy or self.x == 0 or self.y == 0:
            return True
        return False

    def printOutput(self,isLost=False):
        lostText = ""
        if isLost:
            lostText = " LOST"
        return f'({self.x}, {self.y}, {self.orientation})' + lostText