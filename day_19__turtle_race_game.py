##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (24/04/2022)
##  day_19__turtle_race_game
##
##
##########################################################################
import random
from turtle import Turtle,Screen
screen = Screen()

is_race_on = False

colors = ["red","orange","yellow","green","blue","purple"]
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race ? Enter a color : ")
# print(user_bet)
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    penup = new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color =turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations \n You've won the bet ..!! {winning_color} turtle won the game.")
            else:
                print(f"You've lost the bet ..!! {winning_color} turtle won the game.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
