##########################################################################
##
##  Prasad R. Bhosale
##  Saturday (23/04/2022)
##  day_18__hirst_painting_project
##  Draw a random coloured spirograph
##
##########################################################################


#part first to extract color code from image
import colorgram,random
import turtle as t
rgb_colors = []
colors = colorgram.extract('hirst_dot_painting.jpg', 30)
# print(colors)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
# print(rgb_colors)

########################################################
#Part second



t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
