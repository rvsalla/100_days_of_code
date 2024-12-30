from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title='Make your bet', prompt=f'Which turtle will win the race? {colors} enter a color:')
turtle_list = []


for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-200,-150+60*i)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! The {winning_color} turtle was the fastest!")
            else:
                print(f"You Lost! The {winning_color} turtle was the fastest!")
                
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()