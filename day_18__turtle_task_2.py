##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_18__turtle_task 2
##  Draw a dash line
##
##########################################################################

from turtle import Turtle, Screen
import turtle

window  = Screen()
tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

for _ in range(15):
    tim.speed(1)
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


import heroes
print(heroes.gen())     #to create a random hero name

window.exitonclick()
