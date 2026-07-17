# for chess board

def create_board():
    board = [['♖', '♘', '♗', '♕','♔', '♗', '♘', '♖'],
             ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
             ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],]

    # for any operations
    return board

def print_board(board):
    # for a better view of the board/showing the current board in the terminal
    number = 8
    for row in board:
        print("-----------------------------------------", end = "\n| ")
        for piece in row:
            print(f"{piece}", end = "  | ")
        print(number, end = "\n")
        number -= 1
    print("-----------------------------------------\n  ", end = "")
    for i in range(8):
        print(chr(ord('a')+i), end = "    ")