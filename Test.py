from turtle import Turtle, Screen
import time


#Screen settup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Snake body setup
snake = []

for t in range(3):
    snake_segment = Turtle(shape='square')
    snake_segment.color('white')
    snake_segment.penup()
    snake_segment.goto(-20*t,0)
    snake.append(snake_segment)

#Snake movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    
    for seg_num in range(len(snake)-1 , 0 ,-1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(new_x,new_y)
    
    snake[0].forward(20)




screen.exitonclick()