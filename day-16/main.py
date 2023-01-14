#
# from turtle import Turtle, Screen
#
# prince = Turtle()
# print(prince)
# prince.shape('turtle')
# prince.color('chartreuse')
# prince.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtie', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'

print(table)
