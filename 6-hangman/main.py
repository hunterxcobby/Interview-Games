#!/usr/bin/python3


import random 

word_list = ["apple","beautiful", "potato"]
chosen_word = random.choice(word_list)

print(chosen_word)

display = []
lives = 6
is_running = True

for letter in chosen_word:
    display += '_'

print(display)


while is_running:
    guessed_letter = input("Guess a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guessed_letter:
            display[position] == guessed_letter
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            is_running = False 
            print("Game over!")
    if '_' not in display:
        is_running = False
        print("You Win!")