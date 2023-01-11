import pytest
from othello import playable

DIRECTION_xy = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
board = [['□']*8 for _ in range(8)]
board[3][3], board[3][4] = '◎', '●'
board[4][3], board[4][4] = '●', '◎'

def test_playable():
    assert playable('□', DIRECTION_xy, board) == [(2, 3), (3, 2), (4, 5), (5, 4)]