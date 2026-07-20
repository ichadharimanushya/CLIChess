from board import Board
import move
import pieces





# game loop and turn handling


board = Board()





# interaction with the user







while True:
    player_white = input("Enter the name of the player(1) with white pieces: ").strip()
    if player_white: break
print()
while True:
    player_black = input("Enter the name of the player(2) with black pieces: ").strip()
    if player_black: break
print()
print(f"Welcome {player_white} and {player_black}!\n")









lastmove = None
turn = "white"
while True:
    board.print_board()

    # checkmate/stalemate detection logic
    # pass

    # valid input logic
    current_player = player_black if turn == "black" else player_white
    player_move = input(f"{current_player} ({turn})> ").strip().lower()
    if len(player_move) != 5:
        print("Invalid prompt.")
        continue
    player_move = player_move.split()
    if len(player_move) != 2:
        print("Invalid prompt.")
        continue
    player_initial_move = player_move[0]
    player_final_move = player_move[1]
    player_initial_move = move.coordinate_to_index(player_initial_move)
    if player_initial_move is None:
        print("Invalid move choice.")
        continue
    player_final_move = move.coordinate_to_index(player_final_move)
    if player_final_move is None:
        print("Invalid move choice.")
        continue
    game_piece = board.get_piece(player_initial_move[0], player_initial_move[1])
    if game_piece is None:
        print("No piece found at the entered position.")
        continue
    if game_piece.color != turn:
        print("That is not your piece.")
        continue
    possible_moves = game_piece.possible_moves(board, player_initial_move[0], player_initial_move[1], lastmove)
    if player_final_move not in possible_moves:
        print("Unable to move the piece to entered location.")
        continue

    # extra pawn conditions
    if game_piece.symbol in ("♟", "♙"):
        game_piece.has_moved = True
        # if abs(player_final_move[0] - player_initial_move[0]) == 2:
        #     pass      

    # moving the piece
    board.remove_piece(player_initial_move[0], player_initial_move[1])
    if player_final_move[1] != player_initial_move[1] and type(game_piece) == pieces.Pawn and len(possible_moves) != 0:
        if possible_moves[-1] == ():
            board.remove_piece(player_final_move[0]-game_piece.direction, player_final_move[1])
    board.set_piece(player_final_move[0], player_final_move[1], game_piece)
    lastmove = (game_piece, player_final_move, player_initial_move)

    # movement logic
    turn = "black" if turn == "white" else "white"


    





































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

