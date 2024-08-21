#!/usr/bin/python3

import random  # Import the random module to generate random numbers

# Define the range for the guessing game
lowest_num = 1  # The lowest number that can be guessed
highest_num = 100  # The highest number that can be guessed

# Generate a random number within the range that the player will try to guess
answer = random.randint(lowest_num, highest_num)

# Initialize the number of guesses the player has made
guesses = 0

# A flag to control the game loop
is_running = True

# Display the game introduction and instructions to the player
print("Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

# Main game loop - this will continue running until `is_running` is set to False
while is_running:

    # Get input from the player (as a string)
    guess = input("Input your guess:\n")

    # Check if the input is a valid number
    if guess.isdigit():
        # Convert the valid input to an integer
        guess = int(guess)
        
        # Increment the number of guesses by 1
        guesses += 1

        # Check if the guessed number is outside the allowed range
        if guess < lowest_num or guess > highest_num:
            print("Your value is out of range")
            print(f"Please select a number in the range of {lowest_num} and {highest_num}")

        # Check if the guessed number is too low
        elif guess < answer:
            print("Too low, please try again")

        # Check if the guessed number is too high
        elif guess > answer:
            print("Too high, please try again")

        # The player guessed the correct number
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {guesses}")

            # End the game by setting the flag to False
            is_running = False

    # The input was not a valid number
    else:
        print("Invalid value")
        print(f"Select a number between {lowest_num} and {highest_num}")
