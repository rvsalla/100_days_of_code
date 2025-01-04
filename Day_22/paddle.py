from turtle import Turtle
import random

class Paddle(Turtle):

    def __init__(self, coordenates):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid= 1)
        self.setheading(90)
        self.goto(coordenates) 
    
    def up(self):
        self.forward(20)
        
    def down(self):
        self.backward(20)
