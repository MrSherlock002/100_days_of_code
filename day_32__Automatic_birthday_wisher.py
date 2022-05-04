##########################################################################
##
##  Prasad R. Bhosale
##  Wednesday (4/05/2022)
##  day_32__Motivational_quotes_sender
##
##########################################################################
import  smtplib
import datetime as dt
import random
import  pandas

my_email = "prasadbhosale1920@gmail.com"
password = "Prasad@1819"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = r"E:\Stuff\code\Python\100_Days_Of_Code\Birthday+Wisher+(Day+32)+start\Birthday Wisher (Day 32) start\letter_1.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],msg=f"Subject : Happy Birthday..!!\n\n{contents}")

##########################################################################
""" 
DEAR [NAME].

HAPPY BIRTHDAY.!

ALL THE BEST FOR THE YEAR!

Prasad
"""
##########################################################################
"""
name,email,year,month,day
Prasad,prasadbhosale1819@gmail.com,2022,05,04
"""
##########################################################################
                      # Happy Coding #
##########################################################################
