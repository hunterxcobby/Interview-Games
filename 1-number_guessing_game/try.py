#!/usr/bin/python3

import random

lowest_num = 1
highest_num = 100

# welcome the user 
print("Welcome to Number Guessing Game")
print("*******************************\n")

guess = 0 
guesses = 0
is_running = True

answer = random.randint(lowest_num, highest_num)
print(answer)

while is_running:

    print("Please select a number from 1 to 100\n")

    guess = input("Enter number here:> ")

    print(guess)

    if guess.isdigit():
        # this to run
        pass
    else: 
        print("Please enter a valid digit")
