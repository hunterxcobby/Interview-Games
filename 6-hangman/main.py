#!/usr/bin/python3


import random 

word_list = ["apple","beautiful", "potato"]
chosen_word = random.choice(word_list)

print(chosen_word)

display = []

for letter in chosen_word:
    display += '_'

print(display)
guessed_letter = input("Guess a letter: ")