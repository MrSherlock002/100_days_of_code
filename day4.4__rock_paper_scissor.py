##########################################################################
##
##  Prasad R. Bhosale
##  Thursday (07/04/2022)
##  Day 4. project Rock_paper_scissor
##
##########################################################################
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

computer_input = random.randint(0,2)
print(f"Computer select : {computer_input}")
if user_input==computer_input:
    print("Game draw..!!")
elif(computer_input==2) and (user_input==0):
    print("You Win")
    
elif(user_input==2)and (computer_input==1):
    print("You Win")

elif(user_input==1)and (computer_input==0):
    print("You Win")

elif(user_input>2 or user_input<0):
    print("Wrong input.! You lose")

else:
    print("You Lose.!!")
