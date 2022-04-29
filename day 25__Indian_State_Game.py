##########################################################################
##
##  Prasad R. Bhosale
##  Friday (29/04/2022)
##  day 25__Indian_State_Game
##
##########################################################################

import turtle
import  pandas as pd
from datetime import datetime

screen = turtle.Screen()        #to set the window
screen.title("Indian State Game") # To set the title of the window

image = "Indian_states_blank_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.screensize(canvwidth=1200, canvheight=1000)

# # This following step is required to get the co-ordinates of the states
# def mouse_click_coords(x,y):
#     print(x,y)
# # onscreenclick is an event listner
# turtle.onscreenclick (mouse_click_coords)
# # screen.exitonclick()
# screen.mainloop()


data = pd.read_csv("Indian_states.csv")
all_states = data.state.to_list()
guessed_states = []

start_time = datetime.now()
end_time = 0
# print(start_time)

while len(guessed_states) < 37:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/37 States Correct",
                                    prompt="Whats another state's name ? ").title()
    print(answer_state.title())

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
end_time = datetime.now()
# print("End Time : ",end_time)
print(f"You took {end_time-start_time} time.")


##########################################################################
##Indian States.csv

# state,x,y
# Andhra Pradesh,-72.0,-206.0
# Arunachal Pradesh,292.0,173.0
# Assam,260.0,111.0
# Bihar,91.0,76.0
# Chhattisgarh,3.0,-48.0
# Goa,-217.0,-204.0
# Gujarat,-263.0,12.0
# Haryana,-142.0,179.0
# Himachal Pradesh,-119.0,255.0
# Jammu And Kashmir,-165.0,303.0
# Jharkhand,78.0,20.0
# Karnataka,-168.0,-234.0
# Kerala,-149.0,-339.0
# Madhya Pradesh,-104.0,11.0
# Maharashtra,-161.0,-93.0
# Manipur,285.0,68.0
# Meghalaya,216.0,90.0
# Mizoram,265.0,31.0
# Nagaland,299.0,111.0
# Odisha,79.0,-52.0
# Punjab,-161.0,229.0
# Rajasthan,-207.0,112.0
# Sikkim,154.0,131.0
# Tamil Nadu,-92.0,-333.0
# Telangana,-78.0,-132.0
# Tripura,238.0,40.0
# Uttarakhand,-74.0,203.0
# Uttar Pradesh,-39.0,116.0
# West Bengal,142.0,11.0
# Andaman And Nicobar Islands,287.0,-260.0
# Chandigarh,-137.0,225.0
# Dadra And Nagar Haveli,-294.0,-58.0
# Daman And Diu,-239.0,-69.0
# Delhi,-122.0,163.0
# Lakshadweep,-280.0,-285.0
# Puducherry,-58.0,-296.0
# Ladakh,-125.0,322.0


##########################################################################
                            # Happy Coding #
##########################################################################
