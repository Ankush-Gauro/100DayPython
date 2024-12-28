from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.STARTING_POSITION = (0, -280)
        self.shape("turtle")
        self.penup()
        self.color('black')
        self.goto(self.STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
