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
    for letter in chosen_word:
        if letter == guessed_letter:
            print("Match")
        else:
            print("No Match ")