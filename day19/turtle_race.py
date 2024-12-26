from turtle import Turtle, Screen
from random import randint






screen = Screen()
screen.setup(500, 300)
game_on = False
user_bet = screen.textinput("Make your bet", "Which turtle do you think will win?: ").lower()
colors = ["red","orange","yellow","green","blue"]
y_pos = -70
all_turtles = []
for i in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(-230, y_pos)
    y_pos += 30
    all_turtles.append(new_turtle)

if user_bet:
    game_on = True

race_finishers = []

def manage_winners():
    
    for i in range(5):
        print(f"{i+1} is {race_finishers[i]}")

    if race_finishers[0] == user_bet:
        print("You win!")
    else:
        print("You lose")

while game_on:
    if len(race_finishers) > 4:
        manage_winners()
        game_on = False
    for turtle in all_turtles:
        dist = randint(0,10)
        turtle.forward(dist)
        if turtle.xcor() > 210:
            winner_color = turtle.pencolor()
            race_finishers.append(winner_color)
            all_turtles.remove(turtle)









screen.exitonclick()