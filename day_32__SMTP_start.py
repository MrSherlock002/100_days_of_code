##########################################################################
##
##  Prasad R. Bhosale
##  Wednesday (4/05/2022)
##  day_32__SMTP_start
##
##########################################################################

import smtplib
import datetime as dt
import random

my_email = "prasadbhosale1920@gmail.com"
password = "Prasad@1819"
with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email, password=password)
    my_msg=" Subject : Hello this is Prasad\n \n This is a body of a mail.\n Have a nice Day..!!"

    connection.sendmail(from_addr=my_email, to_addrs="prasadbhosale1819@gmail.com",msg=my_msg)
# connection.close()

now=dt.datetime.now()
# print(now)
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2000, month=3, day =6)
print(date_of_birth)

