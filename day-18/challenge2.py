from turtle import Turtle, Screen
import random

# drawing of polygons


def color_selector():
    colors = ['red', 'yellow', 'green', 'blue', 'indigo', 'orchid', 'pink', 'black', 'chartreuse', 'violet']
    color = random.choice(colors)
    return color


tim = Turtle()

tim.speed(1)
triangle = 360 // 3

draw_shape = True
starter = 3
circumference = 360

while draw_shape:
    for num in range(starter):
        if num <= 10:
            tim.right(circumference / starter)
            tim.forward(100)
        else:
            draw_shape = False
    starter += 1
    circumference = 360
    tim.color(color_selector())

screen = Screen()
screen.exitonclick()


# solution 2 lecturer
# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(color_selector())
#     draw_shape(shape_side_n)
