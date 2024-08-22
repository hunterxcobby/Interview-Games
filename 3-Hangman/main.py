#!/usr/bin/python3

import random
from words import word_list

word = random.choice(word_list)

for x in word:
    print("_", end=" ")


#  we need a function to print the hangman 
def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")   
    
    
def print_word(guessed_letters):
    counter = 0
    rightletters= 0

    for char in word_list:
        if (char in guessed_letters):
            print(word_list[counter], end="")
            rightletters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightletters

