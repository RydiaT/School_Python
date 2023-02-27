# Player Behavior

def play(board):
    coords = input("What are the coords of your play? (Hint: row, col) ")

    if coords == "stop":
        return False
    
    coords = coords.split(',')

    target_i = int(coords[0]) - 1
    target_j = int(coords[1]) - 1

    if target_i > len(board) or target_j > len(board):
        print("That is an invalid play.")
        play(board)
    
    board[target_i][target_j] = "X"

    return board