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


board = Board()
board.display()