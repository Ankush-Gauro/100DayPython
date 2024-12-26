from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(50)

def backward():
    tim.backward(50)

def clockwise():
    for i in range(5):
        tim.right(10)
        tim.forward(10)

def anticlockwise():
    for i in range(5):
        tim.left(10)
        tim.forward(10)

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key = "s", fun=backward)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='a', fun=anticlockwise)
screen.onkey(key='c', fun=tim.reset)



screen.exitonclick()

