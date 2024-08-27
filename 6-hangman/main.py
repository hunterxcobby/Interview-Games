#!/usr/bin/python3

# Importing external files: the hangman stages (visuals) and the list of possible words
import hangman_stages
import random 
from word_list import word_list

# Randomly choose a word from the word_list to be the secret word the player has to guess
chosen_word = random.choice(word_list)

# Debugging line: printing the chosen word (you may want to remove this in the final version, 
# because it shows the answer)
print(chosen_word)

# Initialize an empty list `display` to hold the current state of the guessed word (with underscores)
# Example: if chosen_word is "apple", display will be ['_', '_', '_', '_', '_']
display = []

# Set the initial number of lives (chances) the player has to guess the word incorrectly
lives = 6

# Boolean flag to control the loop. The game keeps running while this is `True`
is_running = True

# Create a display of underscores that matches the length of the chosen word
for letter in chosen_word:
    display += '_'

# Show the initial display with all underscores (no letters guessed yet)
print(display)

# Main game loop: Keeps running until the player wins (guesses all letters) or loses (lives reach 0)
while is_running:
    # Prompt the player to guess a letter and ensure it's in lowercase for consistency
    guessed_letter = input("Guess a letter: ").lower()

    # Iterate over the chosen word and check if the guessed letter is in the word
    # For each correct match, replace the underscore in the `display` with the guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]  # Current letter at the position in chosen_word

        # If the guessed letter matches the current letter in the word, update the display
        if letter == guessed_letter:
            display[position] = guessed_letter

    # Print the current state of the word (with guessed letters filled in)
    print(display)
    
    # If the guessed letter is not in the chosen word, the player loses a life
    if guessed_letter not in chosen_word:
        lives -= 1  # Decrease the number of lives by 1
        print(f"You have {lives} lives left")  # Notify the player of their remaining lives

        # If the player runs out of lives (lives == 0), the game ends with a loss
        if lives == 0:
            is_running = False  # Stop the game loop
            print("Game over!")  # Notify the player that they lost
    
    # If there are no more underscores in the display, the player has guessed the word and wins
    if '_' not in display:
        is_running = False  # Stop the game loop
        print("You Win!")  # Notify the player that they won

    # Show the current stage of the hangman (based on remaining lives) to give the player visual feedback
    print(hangman_stages.stages[lives])
