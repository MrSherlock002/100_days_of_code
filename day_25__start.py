##########################################################################
##
##  Prasad R. Bhosale
##  Thursday (28/04/2022)
##  day_25__start
##
##########################################################################

# with open ("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] !="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import  pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

x=(sum(temp_list)/len(temp_list))
print("average_sum = ",x)

print(data["temp"].mean())          #It also does the work same as sum
print(data["temp"].max())

monday = data[data.day =="Monday"]
print(monday.condition)

#Create a dataframe from scratch
data_dict = {"Students" : ["Amy", "James", "Angela"],
             "Scores": [76,56,65]}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
