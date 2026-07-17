from board import Board
import move

# game loop and turn handling



user = input("Enter a move> ")

board = Board()
user = user.split()

initial_square = user[0]
final_square = user[1]

if move.coordinate_to_index(initial_square)is not None and move.coordinate_to_index(final_square) is not None:
    initial_row, initial_col = move.coordinate_to_index(initial_square)
    final_row, final_col = move.coordinate_to_index(final_square)

    print(initial_row, initial_col)

    board.print_board()
    piece = board.remove_piece(initial_row, initial_col)
    if not piece == None:
        board.set_piece(initial_row, initial_col, None)
        board.set_piece(final_row, final_col, piece)
        board.print_board()
    else:
        print("k")