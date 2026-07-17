# move representation (helper functions)

def coordinate_to_index(square = ""):
    xy = square.strip().lower()

    # base case
    if len(xy) != 2: return None    
    if not xy[0].isalpha(): return None
    if not xy[1].isnumeric(): return None

    # coordinate according to the index of board variables
    # return (8-int(xy[1]), ord(xy[0])-ord('a'))
    file = xy[0]
    rank = int(xy[1])

    if not (ord('a') <= ord(file) and ord(file) <= ord('h')):
        return None
    if not (1 <= rank and rank <= 8):
        return None

    row = 8 - rank
    col = ord(file) - ord('a')
    return row, col

def index_to_coordinate(row, col):
    if not (0 <= row and row <= 7): return None
    if not (0 <= col and col <= 7): return None

    file = chr(col + ord('a'))
    rank = str(8 - row)
    return file + rank