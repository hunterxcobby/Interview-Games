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

    def is_winner(self, player):
        for combo in [[1, 2, 3]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    return False 
            if result:
                return True
            
        return False

board = Board()

def player_move():

    move = int(input("(X) Pick a place > "))
    board.update_cell(move, "X")

def ai_move():
    
    move = int(input("(O) Pick a place > "))
    board.update_cell(move, "O")

while True:

    board.display()

    player_move()

    if board.is_winner("X"):
        print("X wins")
    
    board.display()
    ai_move()
    board.display()




