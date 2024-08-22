import random

# Greet the player and give context
print("Welcome to hangman")
print("-------------------------------------------")

# Create a list of words that the program can choose from
wordDictionary = ["sunflower", "house", "diamond", "memes", "yeet", "hello", "howdy", "like", "subscribe"]

### Choose a random word from the wordDictionary
randomWord = random.choice(wordDictionary)

# For each character in the randomWord, print an underscore to represent the hidden word
for x in randomWord:
    print("_", end=" ")

# Function to print the hangman stages depending on the number of wrong guesses
def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")  # Head
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")  # Head
        print("|   |")  # Body
        print("    |")
        print("   ===")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")  # Head
        print("/|  |")  # One arm
        print("    |")
        print("   ===")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")  # Head
        print("/|\ |")  # Both arms
        print("    |")
        print("   ===")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")  # Head
        print("/|\ |")  # Both arms
        print("/   |")  # One leg
        print("   ===")
    elif wrong == 6:
        print("\n+---+")
        print(" O   |")  # Head
        print("/|\  |")  # Both arms
        print("/ \  |")  # Both legs
        print("    ===")

# Function to print the guessed letters and spaces for unguessed ones
def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    # Loop through each character in the randomWord
    for char in randomWord:
        # If the letter has been guessed, display it
        if char in guessedLetters:
            print(randomWord[counter], end=" ")
            rightLetters += 1  # Count how many correct letters have been guessed
        else:
            # If the letter hasn't been guessed yet, print an empty space
            print("_", end=" ")
        counter += 1
    return rightLetters  # Return how many letters are correct

# Function to print the underscores corresponding to the length of the word
def printLines():
    print("\r")
    # Loop through each character of the word to print the underline
    for char in randomWord:
        print("\u203E", end=" ")  # Unicode character for an underline

# Store the length of the word that needs to be guessed
length_of_word_to_guess = len(randomWord)
# Keep track of how many wrong guesses have been made
amount_of_times_wrong = 0
# Track how many guesses have been made overall
current_guess_index = 0
# List to store all the letters that have been guessed by the player
current_letters_guessed = []
# Track the correct guesses so far
current_letters_right = 0

# The main game loop: runs until either 6 wrong guesses are made or the word is fully guessed
while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
    # Display all guessed letters so far
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")

    ### Prompt user for a letter input
    letterGuessed = input("\nGuess a letter: ")

    ### If the guessed letter is in the word, update the board and display the current word
    if letterGuessed in randomWord:
        # Print the hangman figure (this will be unchanged as no wrong guess was made)
        print_hangman(amount_of_times_wrong)
        # Increase the guess index and store the correctly guessed letter
        current_guess_index += 1
        current_letters_guessed.append(letterGuessed)
        # Display the word with correct guesses revealed
        current_letters_right = printWord(current_letters_guessed)
        # Print the underline for aesthetics
        printLines()

    ### If the guessed letter is NOT in the word, update the hangman figure and increment wrong guesses
    else:
        # Increment the wrong guesses count
        amount_of_times_wrong += 1
        # Add the guessed letter to the list of guessed letters
        current_letters_guessed.append(letterGuessed)
        # Update the hangman figure to show the new mistake
        print_hangman(amount_of_times_wrong)
        # Display the word with correct guesses revealed
        current_letters_right = printWord(current_letters_guessed)
        # Print the underline for aesthetics
        printLines()

# Once the game ends, print a thank you message
print("Thank you for playing :)")
