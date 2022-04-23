##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_18__turtle_start
##
##########################################################################

from turtle import Turtle, Screen
import turtle

window  = Screen()
timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.speed(1)
timmy_the_turtle.forward(300)
timmy_the_turtle.right(90)
timmy_the_turtle.speed(1)
timmy_the_turtle.forward(300)


window.exitonclick()
