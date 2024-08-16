#!/usr/bin/python3

import os 
os.system("clear") #for clearing the screen

"""
create a class to show our board
"""

class Board():
    def __init__ (self): 
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
    
    """a function called display to display the board"""
    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player
        
    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        
    def reset(self):
        self.cells = []
        self.cells = [" "," "," "," "," "," "," "," "," "," "]   

board = Board()

def print_header():
    print("Welcome to tic-tac-toe\n")

def refresh_screen():
    # clear the screen
    os.system("clear")

    # print the header
    print_header()

    # display the board
    board.display()




while True:
    refresh_screen()

    # Get X input
    x_choice = int(input("\nX) Please choose 1 - 9. > "))

    #Update the baord
    board.update_cell(x_choice, "X")

    # refresh the screen
    refresh_screen()

    # check for X win
    if board.is_winner("X"):
        print("\n X wins!!!")
        play_again = input("Do you want to play again?(Y/N)")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
        
    # Get X input
    o_choice = int(input("\nO) Please choose 1 - 9. > "))

    #Update the baord
    board.update_cell(o_choice, "0")


