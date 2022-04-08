##########################################################################
##
##  Prasad R. Bhosale
##  Friday (08/04/2022)
##  Day 5.4 Fizzbuzz_program
##
##########################################################################

#Write your code below this row 👇

for i in range(1,101):
    if (i%3==0) and (i%5==0):
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
