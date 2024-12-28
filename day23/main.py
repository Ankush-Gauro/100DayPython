import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(600,600)
screen.tracer(False)
screen.listen()


player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move_cars()

    for c in car.all_cars:
        if player.distance(c) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.goto(player.STARTING_POSITION)
        car.level_up()
        score.add_level()
        score.update_score()


screen.exitonclick()
