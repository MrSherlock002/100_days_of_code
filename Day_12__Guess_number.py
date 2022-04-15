##########################################################################
##  
##  Prasad R. Bhosale  
##  Thursday (14/04/2022)
##  
##  Day_12__Guess_number
## 
##########################################################################


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def guess_game(random_num,lives):
    while(lives!=0):
        num = int(input("Enter a guess : "))
        if random_num<num:
            print("Your guess is high.")
            lives -=1
        elif num<random_num:
            print("Your guess is low.")
            lives -=1
        elif num==random_num:
            print("You win")
    

        
def main():
    lives = 0
    random_num = random.randint(0,100)
    choice = input("Do you want play easy mode or hard mode ? (e/h) ").lower()
    if choice=="e":
        lives = 10
        guess_game(random_num,lives)
    elif choice=="h":
        lives=7
        guess_game(random_num,lives)
    else:
        print("Invalid Input")
    # play_again = input("Do you want to play again ? (1/0)")
    # if play_again=="1":
            
if __name__ == "__main__":
    main()
