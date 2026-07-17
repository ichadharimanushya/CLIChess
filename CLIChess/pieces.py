# ├── pieces/
# │   ├── __init__.py
# │   ├── piece.py          # Base Piece class
# │   ├── pawn.py
# │   ├── rook.py
# │   ├── knight.py
# │   ├── bishop.py
# │   ├── queen.py
# │   └── king.py

class Piece:
    def __init__(self, color):
        self.color = color

    def possible_moves(self, board, row, col):
        pass


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♟" if color == "white" else "♙"
        # -1 for white, as they move up the rows, self-explanatory
        self.direction = -1 if color == "white" else 1

    def possible_moves(self, board, row, col):
        moves = []
        pawn_offset = [
            (0, self.direction), (1, self.direction), (-1, self.direction)
        ]
        for r, c in pawn_offset:
            new_row, new_col = r + row, c + col
            if board.is_valid_position(new_row, new_col):
                target_boxORpiece = board.get_piece(new_row, new_col)
                if target_boxORpiece is None or target_boxORpiece.color != self.color:
                    moves.append((new_row, new_col))
        return moves

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♜" if color == "white" else "♖"

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♝" if color == "white" else "♗"

    def possible_moves(self, board, row, col):
        pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♞" if color == "white" else "♘"

    def possible_moves(self, board, row, col):
        moves = []
        knight_offsets = [
            (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (1, -2), (-1, -2)
        ]
        for r, c in knight_offsets:
            new_row, new_col = r + row, c + col
            if board.is_valid_position(new_row, new_col):
                target_boxORpiece = board.get_piece(new_row, new_col)
                if target_boxORpiece is None or target_boxORpiece.color != self.color:
                    moves.append((new_row, new_col))
        return moves

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♛" if color == "white" else "♕"

    def possible_moves(self, board, row, col):
        pass

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♚" if color == "white" else "♔"

    def possible_moves(self, board, row, col):
        pass

