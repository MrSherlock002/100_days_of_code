##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (24/04/2022)
##  day_19__start
##
##
##########################################################################

from turtle import Turtle, Screen

tim = Turtle()
window = Screen()

def move_forward():
    tim.forward(10)

window.listen()
window.onkey(move_forward, "space")
window.exitonclick()
