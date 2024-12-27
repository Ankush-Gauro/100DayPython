from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        


    def update_scoreboard(self):
        self.clear()
        self.goto(-50,300)
        self.write(f"{self.l_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(0,300)
        self.write("|", align="center", font=("Courier", 24, "normal"))
        self.goto(50,300)
        self.write(f"{self.r_score}", align="center", font=("Courier", 24, "normal"))

    def add_lpoint(self):
        self.l_score += 1

    def add_rpoint(self):
  	    self.r_score += 1

