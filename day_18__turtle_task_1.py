##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_18__turtle_task 1
##  Draw a square 100*100
##
##########################################################################

from turtle import Turtle, Screen
import turtle

window  = Screen()
tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(4):
    tim.speed(1)
    tim.forward(100)
    tim.left(90)

import heroes
print(heroes.gen())     #to create a random hero name

window.exitonclick()
