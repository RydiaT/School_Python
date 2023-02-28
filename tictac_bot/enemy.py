# Enemy Behavior + Win State Checking
from random import randint

max = 0
i = 0

def enemy_play(board):
    global max
    global i    
    max = len(board) ** 2

    row = 0
    col = 0

    while board[row][col] != ' ' and i < max:
        row = randint(0, len(board) - 1)
        col = randint(0, len(board[row]) - 1)
        i += 1

    board[row][col] = "O"

    return board
    
