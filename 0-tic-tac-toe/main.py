#!/usr/bin/python3

import os 
os.system("clear") #for clearing the screen

"""
creae a class to show our board
"""

class Board():
    def __init__ (self): 
        self.cells = [" ","X ","O","X"," "," "," "," "," "]
    
    """a function called display to display the board"""
    def function(self):
        print (" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))