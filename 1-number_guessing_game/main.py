#!/usr/bin/python3

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")