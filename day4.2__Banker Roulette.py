##########################################################################
##
##  Prasad R. Bhosale
##  Thursday (07/04/2022)
##  Day 4.2 Banker Roulette program
##
##########################################################################

# Split string method

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

length = len(names)
# print(length)
test = random.randint(0,length)

print(f"{names[test]} will pay bill.")



