from turtle import Turtle, Screen
from snake import Snake
import time


#Screen settup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Snake body setup
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Snake movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


screen.exitonclick()