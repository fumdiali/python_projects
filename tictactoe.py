import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ","X","O","X","O","X","O","X","O","X"]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1],self.cells[2],self.cells[3]))
        print(" ----------")
        print(" %s | %s | %s " %(self.cells[4],self.cells[5],self.cells[6]))
        print(" ----------")
        print(" %s | %s | %s " %(self.cells[7],self.cells[8],self.cells[9]))

board = Board()

def print_header():
    print("Welcome to my\nTic-Tac-Toe game")

def refresh_screen():
    #clear the screen
    os.system("clear")

    print_header()

    #show the board
    board.display()

while True:
    refresh_screen()

    #get X input
    x_choice = int(input("\nX Please,choose 1 - 9 >"))
