from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score_show()
    
    def score_show(self):
        self.write(f"Score: {self.score}", align="center", font=('courrier', 12))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('courrier', 30))
    
    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_show()
        