##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (24/04/2022)
##  day_19__etch_a_sketch
##
##
##########################################################################

from turtle import Turtle, Screen

tim = Turtle()
window = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

window.listen()
window.onkey(move_forward, "w")
window.onkey(move_backward, "s")
window.onkey(turn_left, "a")
window.onkey(turn_right, "d")
window.onkey(clear,"c")

window.exitonclick()
