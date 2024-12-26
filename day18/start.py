import turtle as t
from random import randint
t.colormode(255)

def colors():
    r_red = randint(0,255)
    r_green = randint(0,255)
    r_blue = randint(0,255)
    l = [r_red,r_green,r_blue]
    return tuple(l)



tim = t.Turtle()
tim.speed("fastest")


def draw(tilt):
    for i in range(int(360/tilt)):
        tim.color(colors())
        tim.circle(100)
        tim.setheading(tim.heading() + tilt)



draw(10)




screen = t.Screen()
screen.exitonclick()