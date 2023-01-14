from turtle import Turtle, Screen
import random

tim = Turtle()


def random_color_gen():
    colors = ['gray', 'dark cyan', 'dark orange', 'chartreuse', 'dodger blue', 'yellow', 'orchid', 'gold', 'sky blue']
    color = random.choice(colors)
    chosen_color = tim.color(color)
    return chosen_color


direction = [0, 90, 180, 270]


def pen_speed():
    tim.pensize(width=10)
    tim.speed(2)


for num in range(100):

    gen_num = random.randint(0, 1)
    tim.pensize(width=50)
    tim.speed('normal')
    if gen_num == 1:
        random_color_gen()
        pen_speed()
        tim.left(random.choice(direction))
    else:
        random_color_gen()
        pen_speed()
        tim.right(random.choice(direction))
    tim.forward(50)


# for _ in range(200):
#     random_color_gen()
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
