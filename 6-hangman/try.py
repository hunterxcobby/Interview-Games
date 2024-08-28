#!/usr/bin/python3

import random

word_list = ['beautiful', 'potato', 'apple']
chosen_word = random.choice(word_list)


print(chosen_word)

display = []
is_running = True

for letter in chosen_word:
    display += '_'

print(display)

while is_running:

    guessed_letter = input("Type a letter: ").lower()

    for letter in range(len(chosen_word)):
        if guessed_letter == chosen_word[letter]:
            print("Match")
        else:
            print("No Match")
    