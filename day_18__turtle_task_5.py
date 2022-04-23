##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_18__turtle_task 5
##  Draw a random colour (r,g,b)
##
##########################################################################

import  turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return  random_color

# colors = ["LightSkyBlue","Burlywood","Gold","Khaki","Chartreuse","Yellow","DarkMagenta","DarkViolet","Navy"]
directions = [0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
