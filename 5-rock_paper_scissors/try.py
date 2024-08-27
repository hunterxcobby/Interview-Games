#!/usr/bin/python3

import random 

user_choice = int(input("Please choose. 0 for Rock , 1 for Paper, 2 for scissors "))
comp_choice = random.randint(0,2)



if user_choice < 1 or user_choice > 2:
    print("You entered an invalid number, YOU LOSE!")
        
else:
    comp_choice = random.randint(0,2)
    print(f"Computer chose {comp_choice}")
    
    if user_choice == comp_choice:
        print("It is a tie game!")

    elif user_choice > comp_choice:
        print("You win !")

    elif comp_choice > user_choice:
        print("You Lose!")
