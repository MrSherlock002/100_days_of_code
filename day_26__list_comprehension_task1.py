##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (1/05/2022)
##  day_26__list_comprehension_task1
##  Sqare all the even elements from list in single line of code
##
##########################################################################

# task 1
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_number = [num**2 for num in numbers if num%2==0]
print(squared_number)
