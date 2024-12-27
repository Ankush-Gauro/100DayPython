from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.tracer(False)
screen.screensize(800,600)
screen.bgcolor("black")
screen.title("Pong game")
screen.listen()


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = ScoreBoard()


screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down,"s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #collision with r_paddle
    if (ball.distance(r_paddle) < 40 and ball.xcor() > 300) or (ball.distance(l_paddle) < 40 and ball.xcor() < -300):
        ball.bounce_x()


    #collision with wall
    if ball.xcor() > 350:
        score.add_lpoint()
        score.update_scoreboard()
        ball.reset_position()
        

    if ball.xcor() < -350:
        score.add_rpoint()
        score.update_scoreboard()
        ball.reset_position()


        
screen.exitonclick()

