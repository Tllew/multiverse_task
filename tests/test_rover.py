from src.rover import Rover
from src.controller import Controller

def testController():
    map = "4 8"
    rovers = ["(2, 3, E) LFRFF","(0, 2, N) FFLFRFF"]
    expected = ["(4, 4, E)",
     "(0, 4, W) LOST"
     ]

    newController = Controller()

    for i, rover in enumerate(rovers):
        movedRover = newController.createRover(map, rover)
        assert expected[i] == movedRover

def testTurn():
    newRover = Rover(1,1,"N","4","8")
    directions = ["L","L","L","L","R","R","R"]
    expected = ["W","S","E","N","E","S","W","N"]
    for i, direction in enumerate(directions):
        newRover.turn(direction)
        assert expected[i] == newRover.orientation

def testForward():
    newRover = Rover(1,1,"N","4","8")
    directions = ["F","F","F"]
    expected = [[1,2],[1,3],[1,4]]
    for i, direction in enumerate(directions):
        newRover.forward()
        assert expected[i] == [newRover.x,newRover.y]

# def testMove():
#     movements = ["FLFFRF","FFLFRFF","LFRFF"]
#     expected = [[-1,2],[0,5],[0,3]]
#     for i, movement in enumerate(movements):
#         newRover = Rover(1,1,"N","4","8")
#         newRover.move(movement)
#         assert expected[i] == [newRover.x,newRover.y]
