import turtle
import random


t = turtle.Turtle()
t.speed('fastest')
turtle.colormode(255)
t.penup()
t.hideturtle()

x = -220
y = -220

for i in range(10):
    t.goto(x,y)
    for j in range(10):
        t.dot(30,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        t.forward(50)
    y += 50

screen = turtle.Screen()
screen.exitonclick()