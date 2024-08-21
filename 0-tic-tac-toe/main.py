#!/usr/bin/python3

import os
import platform  # Import platform to check the operating system (Windows/Linux/Mac)

# Define a class to represent the Tic-Tac-Toe board and its functionalities
class Board:
    def __init__(self):
        # The board is represented by a list of 10 elements (index 0 is unused for easier access)
        # Initializing the board with empty spaces
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Function to display the current state of the board in a 3x3 grid
    def display(self):
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    # Function to update a specific cell with the player's symbol ('X' or 'O')
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            # Only update if the cell is empty
            self.cells[cell_no] = player

    # Function to check if a given player has won the game
    def is_winner(self, player):
        # These are the winning combinations (rows, columns, diagonals)
        for combo in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True  # Assume the player is winning until proven otherwise
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    # If any cell in the combo doesn't belong to the player, set result to False
                    result = False
            if result:
                # If the player occupies all cells in any winning combo, they win
                return True
        return False  # No winning combination found, return False

    # Function to check if the game is a tie (i.e., no empty cells left)
    def is_tie(self):
        used_cells = 0  # Count how many cells are occupied
        for cell in self.cells:
            if cell != " ":  # If the cell is not empty, increment the counter
                used_cells += 1
        if used_cells == 9:  # If all 9 cells are used, it's a tie
            return True
        return False  # Otherwise, the game is not tied

    # Function to reset the board for a new game
    def reset(self):
        # Set all cells back to empty spaces
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Function for AI to make a move (basic AI behavior)
    def ai_move(self, player):
        # Preferentially choose the center if it's free
        if self.cells[5] == " ":
            self.update_cell(5, player)
        else:
            # Otherwise, choose the first available cell from 1 to 9
            for i in range(1, 10):
                if self.cells[i] == " ":
                    self.update_cell(i, player)
                    break  # Stop after making the first valid move

# Function to print the game header
def print_header():
    print("Welcome to Tic-Tac-Toe\n")

# Function to clear the terminal screen (works for both Windows and Unix-like systems)
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")  # Clear the screen for Windows
    else:
        os.system("clear")  # Clear the screen for Unix/Linux/Mac

# Function to refresh the screen (clear it, print header, and display the board)
def refresh_screen():
    clear_screen()  # Clear the screen
    print_header()  # Print the header
    board.display()  # Display the board

# Function to validate user input (ensure it is within the valid range and the cell is empty)
def valid_input(choice):
    return choice in range(1, 10) and board.cells[choice] == " "

# Create a new instance of the Board class to represent the game
board = Board()

# Main game loop (runs continuously until the game ends)
while True:
    refresh_screen()  # Clear and display the current state of the board

    # Get player X's input
    while True:
        try:
            x_choice = int(input("\nX) Please choose 1 - 9: "))
            if valid_input(x_choice):  # Check if the input is valid
                board.update_cell(x_choice, "X")  # Update the board with X's choice
                break  # Exit the loop if a valid move is made
            else:
                print("Invalid move, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")  # Handle invalid input

    refresh_screen()  # Refresh the screen after X's move

    # Check if player X has won the game
    if board.is_winner("X"):
        print("\nX wins!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()  # Reset the board if the player wants to play again
            continue  # Continue to the next iteration of the game loop
        else:
            print("Thank you for playing!")
            break  # Exit the game loop if the player chooses not to play again

    # Check if the game is tied
    if board.is_tie():
        print("\nTie Game!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()  # Reset the board if the player wants to play again
            continue  # Continue to the next iteration of the game loop
        else:
            print("Thank you for playing!")
            break  # Exit the game loop if the player chooses not to play again

    # AI's turn (O)
    board.ai_move("O")  # AI makes its move
    refresh_screen()  # Refresh the screen after AI's move

    # Check if AI (O) has won the game
    if board.is_winner("O"):
        print("\nO wins!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()  # Reset the board if the player wants to play again
            continue  # Continue to the next iteration of the game loop
        else:
            print("Thank you for playing!")
            break  # Exit the game loop if the player chooses not to play again

    # Check if the game is tied
    if board.is_tie():
        print("\nTie Game!!!")
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y":
            board.reset()  # Reset the board if the player wants to play again
            continue  # Continue to the next iteration of the game loop
        else:
            print("Thank you for playing!")
            break  # Exit the game loop if the player chooses not to play again
