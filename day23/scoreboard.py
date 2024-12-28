
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-280,280)
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)
    
    def add_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', font=FONT)


