from pieces import Pawn, Rook, Knight, Bishop, Queen, King

# for chess board
class Board():
    def __init__(self):
        self.board = [[Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
                [Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black")],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white")],
                [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")],]
    
    def get_board(self):
        return self.board

    def print_board(self):  # this function is done, final, packed and sealed.
        number = 8
        for row in self.board:
            print("-----------------------------------------", end = "\n| ")
            for piece in row:
                if piece is None:
                    print(" ", end = "  | ")
                    continue
                print(f"{piece.symbol}", end = "  | ")
            print(number, end = "\n")
            number -= 1
        print("-----------------------------------------\n  ", end = "")
        for i in range(8):
            print(chr(ord('a')+i), end = "    ")
        print()

    def get_piece(self, row, col):  # this function is done, final, packed and sealed.
        return self.board[row][col]

    def remove_piece(self, row, col):   # this function is done, final, packed and sealed.
        piece = self.board[row][col]
        self.board[row][col] = None
        return piece

    def set_piece(self, row, col, piece):   # this function is done, final, packed and sealed.
        self.board[row][col] = piece

    def is_valid_position(self, row, col):      # this function is done, final, packed and sealed.
        return (0 <= row < 8 and 0 <= col < 8)
    
    def get_pieces_of_color(self, color):   # this function is done, final, packed and sealed.
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color == color:
                    pieces.append((row, col, piece))
        return pieces