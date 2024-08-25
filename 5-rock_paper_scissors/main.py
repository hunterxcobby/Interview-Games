#!/usr/bin/python3

import random  # Import the random module to generate a random choice for the computer

# Get the user's choice
# We ask the user to input their choice, which is expected to be 0 (Rock), 1 (Paper), or 2 (Scissors).
user_choice = int(input("Enter your choice. 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

# Check if the user's choice is valid (it must be between 0 and 2 inclusive).
# If it's invalid (i.e., not 0, 1, or 2), print an error message and declare that the user loses.
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number, YOU LOSE!")
else:
    # Generate the computer's choice using the random.randint() function.
    # The computer will randomly choose either 0 (Rock), 1 (Paper), or 2 (Scissors).
    cmp_choice = random.randint(0, 2)
    print(f"Computer chose: {cmp_choice}")  # Print the computer's choice for reference

    # Compare the user's choice and the computer's choice to determine the result.
    # The game logic for Rock-Paper-Scissors works as follows:
    # - Rock (0) beats Scissors (2)
    # - Scissors (2) beats Paper (1)
    # - Paper (1) beats Rock (0)
    # - If both choices are the same, it's a tie.

    # If both the user and the computer chose the same option, it's a tie.
    if cmp_choice == user_choice:
        print("It is a tie")
    
    # If the computer chose Rock (0) and the user chose Scissors (2), the user loses.
    # Rock beats Scissors.
    elif cmp_choice == 0 and user_choice == 2:
        print("You Lose!")
    
    # If the user chose Rock (0) and the computer chose Scissors (2), the user wins.
    # Rock beats Scissors.
    elif user_choice == 0 and cmp_choice == 2:
        print("You Win!")
    
    # If the computer's choice is greater than the user's choice, the user loses.
    # This handles the cases where:
    # - Computer chose Paper (1) and user chose Rock (0)
    # - Computer chose Scissors (2) and user chose Paper (1)
    elif cmp_choice > user_choice:
        print("You Lose!")
    
    # If the user's choice is greater than the computer's choice, the user wins.
    # This handles the cases where:
    # - User chose Paper (1) and computer chose Rock (0)
    # - User chose Scissors (2) and computer chose Paper (1)
    elif user_choice > cmp_choice:
        print("You Win!")
