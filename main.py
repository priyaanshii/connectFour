import os

from player import Player
from board import Board

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main() :
    p1 = Player(symbol="X")
    p2 = Player(symbol="Y")
    board = Board(6,7,[p1,p2])

    while True:
        while True:
            cls()
            board.draw()
            try:
                curCol = int(input(f"Player {board.turn}: "))-1
                if not board.isColValid(curCol):
                    raise Exception
                break
            # We try casting a string to an int
            except ValueError:
                continue

        if board.putPieceAndVerify(curCol):
            cls()
            board.draw()
            print(f"Player {board.turn} has won!")
            break
        board.changeTurn()

main()