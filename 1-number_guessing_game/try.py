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
        guess = int(guess)

        #  if guess is lower than the lowest and 
        # higher than the highest 

        if guess <= 1 or guess > 100:
            print("please make sure number is in range")
        pass
    else: 
        print("Please enter a valid digit")
