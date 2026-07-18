from board import Board
import move
import pieces

# game loop and turn handling

board = Board()

# interaction with the user












































# basic moment logic

# for i in range(10):
#     board.print_board()
#     user = input("Enter a move> ")
#     user = user.split()
#     initial_square = user[0]
#     final_square = user[1]


#     row, col = move.coordinate_to_index(initial_square)
#     possible_moves = pieces.King("white").possible_moves(board, row, col)
#     final_move = move.coordinate_to_index(final_square)
#     print(possible_moves, final_move)
#     if final_move in possible_moves:
#         piece = board.remove_piece(row, col)
#         row, col = move.coordinate_to_index(final_square)
#         board.set_piece(row, col, piece)
#     else:
#         print("Invalid move")

