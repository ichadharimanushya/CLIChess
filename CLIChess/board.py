

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

    # def get_board(self):
    #     return self.board

    def print_board(self):
        # for a better view of the board/showing the current board in the terminal
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

    def get_piece(self, row, col):
        # to get the piece at a position
        return self.board[row][col]

    def remove_piece(self, row, col):
        # to remove a piece form a postition and return it
        piece = self.board[row][col]
        self.board[row][col] = ' '
        return piece

    def set_piece(self, row, col, piece):
        # to set a piece to a potition
        self.board[row][col] = piece

    def is_valid_position(self, row, col):
        return (0 <= row < 8 and 0 <= col < 8)
    
    
Board().print_board()