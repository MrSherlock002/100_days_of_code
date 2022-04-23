##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_18__turtle_task 4
##  Draw a random coloured walk
##
##########################################################################

import  turtle as t
import random
tim = t.Turtle()

colors = ["LightSkyBlue","Burlywood","Gold","Khaki","Chartreuse","Yellow","DarkMagenta","DarkViolet","Navy"]
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(100):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
