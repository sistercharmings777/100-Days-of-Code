import turtle
import turtle as t
import colorgram
import random


# tim.speed('fastest')
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for num in range(len(colors)):
#     r = colors[num].rgb.r
#     g = colors[num].rgb.g
#     b = colors[num].rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)
tim = t.Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
color_list = [
    (239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
    (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
    (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
    (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
    (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)
]
tim.speed(3)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
