#!/usr/bin/python3

import random

user_choice = int(input("Enter your choice. 0 for Rock, 1 for Paper, 2 for scissors: \n"))

if user_choice >= 3 or user_choice < 1:
    print("You entered an invalid number, YOU LOSE!")
else:
    cmp_choice = random.randint(0,2)
    print(cmp_choice)

    # Print the conditions in this particular order to ensure game works fine 
    if cmp_choice == user_choice:
        print("It is a tie")
    elif cmp_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif user_choice == 0 and cmp_choice == 2:
        print("You Win!")
    elif cmp_choice > user_choice:
        print("You Lose!")
    elif user_choice > cmp_choice:
        print("You Win!")
