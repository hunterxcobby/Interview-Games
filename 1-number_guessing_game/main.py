#!/usr/bin/python3

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Input your guess:\n")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Your value is out of range")
            print(f"Please select a number in the range of {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low, please try again")
        elif guess > answer:
            print("Too high, please try again")
        else:
            print(f"CORRECT !  The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid value")
        print(f"Select a number between {lowest_num} and {highest_num}")