#!/usr/bin/python3

import random
from hangman_stages import stages

word_list = ['beautiful', 'potato', 'apple']
chosen_word = random.choice(word_list)


print(chosen_word)

display = []
is_running = True
lives = 6

for letter in chosen_word:
    display += '_'

print(display)

while is_running:

    guessed_letter = input("Type a letter: ").lower()

    for letter in range(len(chosen_word)):
        if guessed_letter == chosen_word[letter]:
            display[letter] = guessed_letter
    
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left")
    if lives == 0:
        print("Game Over")
        is_running = False
    else:
        print(display)
    
    if '_' not in display:
        print("You have won!")
        is_running = False

    print(stages[lives])