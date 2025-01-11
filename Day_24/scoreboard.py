from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score_show()
    
    def score_show(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=('courrier', 16))

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.save_high_score(self.score)
        self.score = 0
        self.score_show()
    
    def save_high_score(self, score):
        with open(".\Day_24\high_score.txt", mode= "w") as score_file:
            score_file.write(str(score))
    
    def read_high_score(self):
        with open(".\Day_24\high_score.txt", mode= "r") as score_file:
            return int(score_file.read())
    
    def score_increase(self):
        self.score += 1
        self.score_show()
        