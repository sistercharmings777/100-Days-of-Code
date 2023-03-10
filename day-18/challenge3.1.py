import turtle as t
from turtle import Screen
import random

# random walk generator

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


direction = [0, 90, 180, 270]

tim.pensize(width=15)
tim.speed('fastest')

for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
