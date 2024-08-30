#!/usr/bin/python3

import os
os.system("clear")

class Board():

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " "," ", " ", " ", " ", " ",]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))


    def update_cell(self, cell_no, player):
        # only update it if it is empty
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True

    def is_tie(self):
        used_cells = 0
        for cells in self.cells:
            if cells != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset_board(self):
        self.cells = [" ", " ", " ", " ", " "," ", " ", " ", " ", " ",]


board = Board()


def header():
    print("Welcome to Tic Tac Toe\n")

def refresh():

    # clear the screen
    os.system("clear")
    # print the header
    header()

    # display the board
    board.display()


while True:

    refresh()

    # take X input
    x_choice = int(input("(X) Choose a number from 1-9: "))

    # update board
    board.update_cell(x_choice, "X")

    # check for x win 
    if board.is_winner("X"):
        print("X wins")
        play_again = input("Do you want to play again? Y/N ").upper()
        if play_again == "Y":
            board.reset_board()
            continue
        else:
            break

    refresh()

    # take X input
    o_choice = int(input("(O) Choose a number from 1-9: "))

    # update board
    board.update_cell(o_choice, "O")

    # check for o win 
    if board.is_winner("O"):
        print("O wins")
        play_again = input("Do you want to play again? Y/N ").upper()
        if play_again == "Y":
            board.reset_board()
            continue
        else:
            break

    refresh()


