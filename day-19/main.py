import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def move_upward():
    tim.left(20)


def move_downward():
    tim.right(20)


def clear_movement():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


turtle.onkey(fun=move_forward, key='w')
turtle.onkey(fun=move_backward, key='s')
turtle.onkey(fun=move_upward, key='a')
turtle.onkey(fun=move_downward, key='d')
turtle.onkey(fun=clear_movement, key='c')

screen.listen()
screen.exitonclick()
