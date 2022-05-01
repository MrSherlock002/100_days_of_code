##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (1/05/2022)
##  day_26__Dictionary_Comprehension_learn.py
##
##########################################################################

import  random
names = ["Alex", "Beth","Dave", "Caroline","Freddie","Eleanor"]

# student_scores = {new_key : new_value for item in names }
student_scores = {student : random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student :score for (student,score) in student_scores.items() if score >=50}
print(passed_students)
