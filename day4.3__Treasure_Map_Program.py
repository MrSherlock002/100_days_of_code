##########################################################################
##
##  Prasad R. Bhosale
##  Thursday (07/04/2022)
##  Day 4.3. Treasure Map Program
##
##########################################################################

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
temp = []
for i in str(position):
    temp.append(i)
print(temp)

column = int(temp[0])
row = int(temp[1])
map[row][column]= "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
