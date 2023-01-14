from turtle import Turtle, Screen

princess = Turtle()

for _ in range(15):
    princess.forward(5)
    princess.penup()
    princess.forward(5)
    princess.pendown()


screen = Screen()
screen.exitonclick()