from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in positions:
    t = Turtle(shape='square')
    t.color('white')
    t.penup()
    t.goto(position)
    segments.append(t)


game_on = True

while game_on:
    screen.update()
    for segment in segments:
        segment.forward(20)








screen.exitonclick()

