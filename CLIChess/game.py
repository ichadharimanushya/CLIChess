from board import Board
import move

# game loop and turn handling



user = input("Enter a move> ")

board = Board()
user = user.split()

initial_square = user[0]
final_square = user[1]

initial_row, initial_col = move.coordinate_to_index(initial_square)
final_row, final_col = move.coordinate_to_index(final_square)

print(initial_row, initial_col)

# board.get_piece(initial_row, initial_col)
# board.remove_piece()