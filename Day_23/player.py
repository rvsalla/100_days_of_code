from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.position_reset()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def win(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
    def position_reset(self):
        self.goto(STARTING_POSITION)
        