#!/usr/bin/python3

import random 

user_choice = int(input("Please choose. 0 for Rock , 1 for Paper, 2 for scissors "))
comp_choice = random.randint(0,2)
print(comp_choice)


if user_choice < 1 or user_choice > 2:
    print("You entered an invalid number, YOU LOSE!")


