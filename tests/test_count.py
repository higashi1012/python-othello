from othello import count


def test_count():
    piece = 'BLACK'
    board = [['BLACK', 'BLACK', 'WHITE', 'BLACK']]
    assert count(piece, board) == 3