from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveforward():
    tim.forward(10)

screen.listen()
screen.onkey(key='space', fun=moveforward)

screen.exitonclick()




