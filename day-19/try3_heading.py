import turtle

turtle.speed(1)

for i in range(4):
    turtle.forward(100)

    var = turtle.heading()

    turtle.write(str(var))
    turtle.backward(100)
    turtle.left(90)