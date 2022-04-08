##########################################################################
##
##  Prasad R. Bhosale
##  Friday (08/04/2022)
##  Day 5.1__Average_height_calculator
##
##########################################################################



# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
    
#Write your code below this row 👇
    sum = sum+student_heights[n]

avg = sum/len(student_heights)
print("Average height = ",avg)



