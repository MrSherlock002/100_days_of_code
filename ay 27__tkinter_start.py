##########################################################################
##
##  Prasad R. Bhosale
##  Monday (2/05/2022)
##  day 27__tkinter_start
##
##########################################################################

from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

#Label
my_label = Label(text = "I am a label.",font=("Arial",24,"bold"))
# my_label.pack(side="left")
my_label.pack(side="top")
# my_label.pack(expand = True)
my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    # my_label["text"] = "Button Got Clicked"

button = Button(text="Click me",command=button_clicked)
button.pack()

# Entry
input = Entry(width=50)
input.pack()
print(input.get())

window.mainloop()

#
# #Adding the turtle
# import  turtle
#
# tim = turtle.Turtle()
# screen = turtle.Screen()
# tim.hideturtle()
# tim.write("Some Text", font=("Times New Roman",40,"bold"))
# screen.exitonclick()

# def add(*args):
#     # print(args)
#     sum = 0
#     print(type(args))
#     for n in args:
#         sum+= n
#     return sum
#
# ans=add(1,2,3,4)
# print(ans)
#
# def calculate(n,**kwargs):
#     print(kwargs)
#     # for key,value in kwargs.items():
#         # print(key)
#         # print(value)
#     n +=kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#     print(kwargs["add"])
# calculate(2,add=3,multiply=5)
#
#
# class Car:
#     def __init__(self,**kw):
#         # self.make = kw["make"]
#         # self.model = kw ["model"]
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
# my_car = Car(make="Safari")
# print(my_car.model)
#
# def all_a(a,*args,**kw):
#     print(a,args,kw)
# all_a(4,7,3,0,x=10,y=64)
