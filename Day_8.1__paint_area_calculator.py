##########################################################################
##
##  Prasad R. Bhosale
##  Monday (11/04/2022)
##  Day_8.1__paint_area_calculator
##
##########################################################################


#Write your code below this line 👇
import math 

def paint_calc(height, width, cover):
    result = ((height*width)/cover)
    print(f"You need total number of paint cans = {math.ceil(result)}")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
