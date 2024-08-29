#!/usr/bin/python3


class Board():

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " "," ", " ", " ", " ", " ",]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("------------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("------------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))


    def update_cell(self, cell_no, player):
        # only update it if it is empty
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

board = Board()

board.update_cell(4, "X")

board.display()


