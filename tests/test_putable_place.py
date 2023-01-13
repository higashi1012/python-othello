import pytest
from board import Board

board = Board()

def test_putable_places():
    assert board.putable_places('●') == [(2, 3), (3, 2), (4, 5), (5, 4)]
    assert board.putable_places('◎') == [(2, 4), (3, 5), (4, 2), (5, 3)]