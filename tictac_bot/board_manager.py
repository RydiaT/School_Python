from player import play

def write_to_log(str):
    file = open("log_history.txt", "a")
    file.write(str + "\n")
    file.close

def generate_board(size):
    board = []

    i = 0
    while i < size:
        board.append([])
        j = 0
        while j < size:
            board[i].append(' ')
            j += 1
        i += 1
    
    return board

def draw_board(board):
    text_board = ''

    i = 0
    while i < len(board):
        j = 0
        while j < len(board):
            text_board += f"[{board[i][j]}]"
            j += 1
        text_board += "\n"
        i += 1

    return text_board

def setup_board(size):
    board = generate_board(size)

    print(draw_board(board))

    while True:
        board = play(board)
        if not board:
            print("Goodbye")
            break
        print(draw_board(board))
