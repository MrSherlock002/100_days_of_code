##########################################################################
##
##  Prasad R. Bhosale
##  Monday (2/05/2022)
##  day_27__tkinter_miles_to_km_project
##
##########################################################################

from tkinter import *

def miles_to_km():
    miles =float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

# miles_input = DoubleVar()
miles_input = DoubleVar()
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# miles_to_km()
window.minsize(width=500, height=300)


calculate_button = Button(text="Calculate", commmand=miles_to_km)
calculate_button.grid(column=1, row=2)
window.mainloop()
