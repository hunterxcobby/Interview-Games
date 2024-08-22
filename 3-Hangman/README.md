### Code Breakdown by Functionality

- **Imports and Setup:**
  - The `random` library is imported to select a random word from the list `wordDictionary`.
  - The game welcomes the player and chooses a random word from the dictionary.
  
- **Hangman Graphics (`print_hangman` function):**
  - Depending on the number of incorrect guesses, different stages of the hangman are drawn.

- **Word and Letter Tracking:**
  - `printWord`: Displays the correctly guessed letters and underscores for the letters that haven't been guessed yet.
  - `printLines`: Prints a line under each letter for visual separation.

- **Main Game Loop:**
  - The loop continues until the player either guesses the word or makes 6 wrong guesses (leading to a complete hangman).
  - Each guess is checked:
    - If correct, it is added to the displayed word.
    - If incorrect, the hangman drawing is updated.

- **Ending the Game:**
  - When the loop exits (either due to all letters being guessed or the hangman being fully drawn), a final message is printed thanking the player.
