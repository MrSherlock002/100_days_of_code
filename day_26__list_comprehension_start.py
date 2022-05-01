##########################################################################
##
##  Prasad R. Bhosale
##  Sunday (1/05/2022)
##  day_26__list_comprehension_start
##
##########################################################################

# new_list = [new_item for item in list]
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
name = "Angela"

letters_list = [letter for letter in name]
print(letters_list)


num_list = [num*2  for num in range(1,5)]
print(num_list)

names = ["Alex", "Beth","Dave", "Caroline","Freddie","Eleanor"]

short_names = [name for name in names if (len(name) < 5)]
print(short_names)

long_names = [name for name in names if (len(name) > 5)]

upper_names = [name.upper() for name in names]
print(upper_names)
