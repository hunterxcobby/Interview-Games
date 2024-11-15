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

print("Please select a number from 1 to 100\n")

while is_running:


    guess = input("Enter number here:> ")

    print(guess)

    if guess.isdigit():
        guess = int(guess)

        guesses += 1
        #  if guess is lower than the lowest and 
        # higher than the highest 

        if guess <= 1 or guess > 100:
            print("please make sure number is in range")
        elif guess > answer:
            print("Number too high, Try Again")
        elif guess < answer:
            print("Number too low, Try Again ")
        else: 
            print("You are correct")
            print(f"You made {guesses} number of guesses")
            is_running = False
    else: 
        print(f"The Digit is invalid, please select a number between {lowest_num} and {highest_num}")
