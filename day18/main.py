import random
import turtle



colors = []
for i in range(10):
    r = random.random()
    b = random.random()
    g = random.random()
    color = (r,b,g)
    colors.append(color)
print(colors)

tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(222)
tim.forward(250)
tim.setheading(0)
n_dots = 100

for dot in range(1, n_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)








screen = turtle.Screen()
screen.exitonclick()