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

    def possible_moves(self, board, row, col, last_move):
        pass

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♟" if color == "white" else "♙"
        # -1 for white, as they move up the rows, self-explanatory
        self.direction = -1 if color == "white" else 1
        self.has_moved = False

    def possible_moves(self, board, row, col, last_move):
        if self.has_moved == False: moves = [(row + 2*(self.direction), col), (row + self.direction, col)]
        else: moves = [(row + self.direction, col)]
        if col == 0:
            diagonal = board.get_piece(row + self.direction, col+1)
            if diagonal is not None and diagonal.color != self.color:
                moves.append((row +self.direction, col + 1))
        elif col == 7:
            diagonal = board.get_piece(row + self.direction, col-1)
            if diagonal is not None and diagonal.color != self.color:
                moves.append((row +self.direction, col - 1))
        else:
            diagonal = board.get_piece(row + self.direction, col+1)
            if diagonal is not None and diagonal.color != self.color:
                moves.append((row +self.direction, col + 1))
            diagonal = board.get_piece(row + self.direction, col-1)
            if diagonal is not None and diagonal.color != self.color:
                moves.append((row +self.direction, col - 1))
        if last_move is None: return moves
        elif type(last_move[0]) == Pawn and last_move[0].color != self.color:
            final = last_move[1]
            initial = last_move[2]
            if (initial[0] in (1, 6)) and (final[0] in (3, 4)):
                if row == final[0] and abs(final[1]-col) == 1:
                    target = ((final[0]+initial[0])//2, initial[1])
                    moves.append(target)
        return moves

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♜" if color == "white" else "♖"

    def possible_moves(self, board, row, col, last_move):
        pass


        # using raytracing for path generation for the pieces

        


        # moves = []
        # rook_offset = [
        #     (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
        #     (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
        #     (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
        #     (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        # ]
        # for r, c in rook_offset:
        #     new_row, new_col = r + row, c + col
        #     if board.is_valid_position(new_row, new_col):
        #         target_boxORpiece = board.get_piece(new_row, new_col)
        #         if target_boxORpiece is None or target_boxORpiece.color != self.color:
        #             moves.append((new_row, new_col))
        # return moves

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♝" if color == "white" else "♗"

    def possible_moves(self, board, row, col, last_move):
        moves = []
        bishop_offset = [
            (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)
        ]
        for r, c in bishop_offset:
            new_row, new_col = r + row, c + col
            if board.is_valid_position(new_row, new_col):
                target_boxORpiece = board.get_piece(new_row, new_col)
                if target_boxORpiece is None or target_boxORpiece.color != self.color:
                    moves.append((new_row, new_col))
        return moves

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♞" if color == "white" else "♘"

    def possible_moves(self, board, row, col, last_move):
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

    def possible_moves(self, board, row, col, last_move):
        moves = []
        queen_offset = [
            (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
            (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
            (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]
        for r, c in queen_offset:
            new_row, new_col = r + row, c + col
            if board.is_valid_position(new_row, new_col):
                target_boxORpiece = board.get_piece(new_row, new_col)
                if target_boxORpiece is None or target_boxORpiece.color != self.color:
                    moves.append((new_row, new_col))
        return moves

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♚" if color == "white" else "♔"

    def possible_moves(self, board, row, col, last_move):
        moves = []
        queen_offset = [
            (-1, -1), (1, -1), (1, 1), (-1, 1), (-1, 0), (0, -1), (1, 0), (0, 1)
        ]
        for r, c in queen_offset:
            new_row, new_col = r + row, c + col
            if board.is_valid_position(new_row, new_col):
                target_boxORpiece = board.get_piece(new_row, new_col)
                if target_boxORpiece is None or target_boxORpiece.color != self.color:
                    moves.append((new_row, new_col))
        return moves

