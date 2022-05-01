##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (1/05/2022)
##  day_26__Dictionary_Comprehension_2
##
##########################################################################
import  pandas

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {new_key : new_value for item in list}
result = {word :len(word) for word in sentence.split()}
print(result)


##Task 3

weather_c = {"Monday" : 12, "Tuesday" : 14, "Wednesday" : 15, "Thursday" : 14, "Friday" : 21, "Saturday":22,"Sunday":24 }

# result1 = {new_key : new_value for item in list}
result1 = {day : (temp_c*9/5)+32 for (day,temp_c)in weather_c.items()}
print(result1)

## Task 4

student_dict = {"student" : ["Angela","James","Lily"],"score": [56,76,98]}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
