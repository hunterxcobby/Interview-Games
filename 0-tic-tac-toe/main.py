#!/usr/bin/python3

import os
import platform

class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        for combo in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
            if result:
                return True
        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def ai_move(self, player):
        if self.cells[5] == " ":
            self.update_cell(5, player)
        else:
            for i in range(1, 10):
                if self.cells[i] == " ":
                    self.update_cell(i, player)
                    break


def print_header():
    print("Welcome to Tic-Tac-Toe\n")


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def refresh_screen():
    clear_screen()
    print_header()
    board.display()


def valid_input(choice):
    return choice in range(1, 10) and board.cells[choice] == " "


board = Board()

while True:
    refresh_screen()

    # Get X input
    while True:
        try:
            x_choice = int(input("\nX) Please choose 1 - 9: "))
            if valid_input(x_choice):
                board.update_cell(x_choice, "X")
                break
            else:
                print("Invalid move, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

    refresh_screen()

    # Check for X win
    if board.is_winner("X"):
        print("\nX wins!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            print("Thank you for playing!")
            break

    # Check for tie
    if board.is_tie():
        print("\nTie Game!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            print("Thank you for playing!")
            break

    # AI's turn (O)
    board.ai_move("O")
    refresh_screen()

    # Check for O win
    if board.is_winner("O"):
        print("\nO wins!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            print("Thank you for playing!")
            break

    # Check for tie
    if board.is_tie():
        print("\nTie Game!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            print("Thank you for playing!")
            break
