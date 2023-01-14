from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# names = ['tim', 'rim', 'jim', 'cim', 'jin', 'min']

# pos_y = -150
#
# for num in range(6):
#     names[num] = Turtle(shape='turtle')
#     names[num].penup()
#     names[num].color(colors[num])
#     names[num].goto(x=-230, y=pos_y)
#     pos_y += 50
#

y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle won.")
            else:
                print(f"You've lost. The {winning_color} turtle won")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
