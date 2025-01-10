import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()

    cars.create_car()
    
    #Detect crossisg
    if turtle.win():
        score.score_increase()
        turtle.position_reset()
        cars.level_up()
    
    #Detect collision with cars
    for car in cars.cars:
        if turtle.distance(car) < 22:
            game_is_on = False
            score.game_over()

screen.exitonclick()