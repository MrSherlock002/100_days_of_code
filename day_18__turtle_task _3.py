##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_18__turtle_task 3
##  Draw a all type of shapes with different colors
##
##########################################################################

import  turtle as t
import random
tim = t.Turtle()

num_sides = 3

colors = ["LightSkyBlue","Burlywood","Gold","Khaki","Chartreuse","Yellow","DarkMagenta","DarkViolet","Navy"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

