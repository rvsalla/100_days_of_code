from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for t in range(3):
            segment = -20*t
            self.add_segment((-20*t,0))

    def add_segment(self,position):
        snake_segment = Turtle(shape='square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake.append(snake_segment)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    
    def extend(self): #add a new segmente to the snake
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake)-1 , 0 ,-1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
    
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != 270: 
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90: 
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0: 
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180: 
            self.head.setheading(0)