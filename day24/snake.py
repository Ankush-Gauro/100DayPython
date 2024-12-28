from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
            self.segments = []
            self.create_snake()
            self.head = self.segments[0]
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            x_pos = self.segments[seg - 1].xcor()
            y_pos = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_pos, y_pos)
        self.head.forward(MOVE)

    def add_segment(self,position):
        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)
            

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
