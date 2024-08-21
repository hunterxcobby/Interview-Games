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

        for combo in [[1,2,3], [3, 4, 5], [7,8,9],[1,4,7], [2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False

            if result == True:
                return True
               
        # if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
        #     return True
        
        # if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
        #     return True
        
        # if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
        #     return True
        
        # if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
        #     return True
        
        # if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
        #     return True
        
        # if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
        #     return True
        
        # if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
        #     return True
        
        # if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
        #     return True


        # return False


    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells =+ 1
        if used_cells == 9:
            return True
        else:
            return False

        
    def reset(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]  

    def ai_move(self, player):
        
        # check if the center is open then choose that
        if self.cells[5] == " ":
            self.update_cell(5, player)
        
        # Ai can win


        # Ai blocks

        #choose random
        for i in range(1, 10):
            if self.cells[i] == " ":
                self.update_cell(i, player)
                break

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
        
    
    # check for a tie
    if board.is_tie():
        print("\n Tie Game!!!")
        play_again = input("Do you want to play again?(Y/N)")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    
    # Get X input
    # o_choice = int(input("\nO) Please choose 1 - 9. > "))

    #Update the baord
    # board.update_cell(o_choice, "O")

    board.ai_move("O") # Ai move O

    refresh_screen()

    # check for O win
    if board.is_winner("O"):
        print("\n O wins!!!")
        play_again = input("Do you want to play again?(Y/N)")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
        
        # check for a tie
    if board.is_tie():
        print("\n Tie Game!!!")
        play_again = input("Do you want to play again?(Y/N)")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break


