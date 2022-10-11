from src.rover import Rover


class Controller:
    def createRover(self, mapText, roverText):
        mapValues = self.parseMapInput(mapText)
        roverInfo, movementText = self.parseRoverInput(roverText)
        newRover = Rover(
            x=roverInfo[0],
            y=roverInfo[1],
            orientation=roverInfo[2],
            mapx=mapValues[0],
            mapy=mapValues[1],
        )
        return newRover.move(movementText)

    def parseMapInput(self, text):
        return text.split(" ")

    def parseRoverInput(self, text):
        splitValues = text.split(") ")
        roverValues = splitValues[0][1:].split(", ")
        movementText = splitValues[1]
        return roverValues, movementText

    def main(self):
        map = input("Input Map Size :>")
        while True:
            rover = input("Input Rover Values :>")
            movedRover = self.createMoveRover(map,rover)
            print(movedRover)


if __name__ == "__main__":
    controller = Controller()
    controller.main()
