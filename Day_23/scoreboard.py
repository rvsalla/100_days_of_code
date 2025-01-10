FONT = ("Courier", 20, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-220,250)
        self.score_show()
    
    def score_show(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
    
    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_show()
