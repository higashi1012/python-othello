piece = 'BLACK'
board = [['BLACK','BLACK','WHITE','BLACK']]

def count(piece, board):
    return sum(cell == piece for row in board for cell in row)

def test_count(piece, board):
    return sum(cell == piece for row in board for cell in row)
assert count('BLACK', board) == 3