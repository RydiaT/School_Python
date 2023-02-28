# Enemy Behavior + Win State Checking
from random import randint

def enemy_play(board):

    row = 0
    col = 0

    while board[row][col] != ' ':
        row = randint(0, len(board) - 1)
        col = randint(0, len(board[row]) - 1)


    board[row][col] = "O"

    return board
    


def checkWin(board, symbol):
    winningStates = []

    # Left To Right
    # For every row, check its column

    i = 0
    while i < len(board):

        rowChecks = []

        j = 0

        while j < len(board):

            if board[i][j] == symbol:
                rowChecks.append(True)
            else:
                rowChecks.append(False)

            j += 1
        
        if rowChecks.__contains__(False):
            winningStates.append(False)
        else:
            winningStates.append(True)
        
        i += 1
    
    if not winningStates.__contains__(False):
        print("Left and Right")
        return True
    
    # Up and Down
    # For every column, check it's row.

    winningStates = []

    j = 0
    while j < len(board):
        colChecks = []
        i = 0
        while i < len(board):
            if board[i][j] == symbol:
                colChecks.append(True)
            else:
                colChecks.append(False)
            
            i += 1
        
        if colChecks.__contains__(False):
            winningStates.append(False)
        else:
            winningStates.append(True)

        j += 1
    
    if not winningStates.__contains__(False):
        print("Up and Down")
        return True
    
    # Crosses - Left to Right
    # Fun fact: Since we have a square board, we only need i to give us a point for this.

    i = 0
    crossChecks = []

    while i < len(board):
        if board[i][i] == symbol:
            crossChecks.append(True)
        else:
            crossChecks.append(False)
        i += 1
    
    if not crossChecks.__contains__(False):
        print("Crosses - Left to Right")
        return True
    
    # Crosses - Right to Left
    # Same thing, but iterate backwards.

    i = 0
    crossChecks = []

    while i < len(board):
        if board[(len(board) - 1 ) - i][(len(board) - 1 ) - i] == symbol:
            crossChecks.append(True)
        else:
            crossChecks.append(False)
        i += 1

    if not crossChecks.__contains__(False):
        print("Crosses - Right to Left")
        return True
    

    return False