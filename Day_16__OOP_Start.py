# ##########################################################################
# ##
# ##  Prasad R. Bhosale
# ##  Sunday (17/04/2022)
# ##  Day_16__OOP_Start
# ##
# ##########################################################################

# import another_module
# print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(200)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# print("| Pokemon |")


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

table.align = "l"
print(table)

table.align = "r"
print(table)


