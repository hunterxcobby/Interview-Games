### Explanation of Each Section:

1. **Imports and Initialization:**
   ```python
   import random
   ```
   - We import the `random` module to generate a random integer for the player to guess.

   ```python
   lowest_num = 1
   highest_num = 100
   ```
   - We define the range of numbers within which the player will guess.

   ```python
   answer = random.randint(lowest_num, highest_num)
   ```
   - `random.randint(lowest_num, highest_num)` generates a random integer between 1 and 100, which will be the answer that the player needs to guess.

   ```python
   guesses = 0
   is_running = True
   ```
   - We initialize a counter `guesses` to keep track of how many guesses the player has made.
   - `is_running` is a flag that controls whether the game is still running or not. It's used to keep the loop going until the player guesses the correct number.

2. **Introduction and Instructions:**
   ```python
   print("Number Guessing Game")
   print(f"Select a number between {lowest_num} and {highest_num}")
   ```
   - These lines display a welcome message and instructions to the player about the range of valid numbers.

3. **Main Game Loop:**
   ```python
   while is_running:
   ```
   - The loop continues running until `is_running` is set to `False`. This happens when the player guesses the correct number.

4. **Player Input and Validation:**
   ```python
   guess = input("Input your guess:\n")
   ```
   - We prompt the player to enter their guess. Since `input()` returns a string, we need to validate that it is a valid number before converting it to an integer.

   ```python
   if guess.isdigit():
   ```
   - The `.isdigit()` method checks if the input consists of digits (i.e., it's a valid positive integer). If it's valid, we proceed to convert the input to an integer.

5. **Game Logic:**
   ```python
   guess = int(guess)
   guesses += 1
   ```
   - We convert the valid input to an integer and increment the number of guesses by 1.

   ```python
   if guess < lowest_num or guess > highest_num:
       print("Your value is out of range")
       print(f"Please select a number in the range of {lowest_num} and {highest_num}")
   ```
   - This checks if the guessed number is outside the allowed range (i.e., less than `lowest_num` or greater than `highest_num`). If it is, the player is informed that their guess is invalid, and the game continues without counting this as a valid guess.

   ```python
   elif guess < answer:
       print("Too low, please try again")
   ```
   - If the guess is valid but less than the correct answer, we inform the player that their guess is too low, and they should try again.

   ```python
   elif guess > answer:
       print("Too high, please try again")
   ```
   - Similarly, if the guess is greater than the correct answer, the player is informed that their guess is too high.

6. **Correct Guess:**
   ```python
   else:
       print(f"CORRECT! The answer is {answer}")
       print(f"Number of guesses: {guesses}")
       is_running = False
   ```
   - If the player's guess matches the correct answer, we inform them that they guessed correctly and display the number of guesses they made. The `is_running` flag is set to `False`, which exits the loop and ends the game.

7. **Handling Invalid Inputs:**
   ```python
   else:
       print("Invalid value")
       print(f"Select a number between {lowest_num} and {highest_num}")
   ```
   - If the player's input is not a number (e.g., they enter letters or special characters), we inform them that their input is invalid and remind them to enter a number between 1 and 100.

