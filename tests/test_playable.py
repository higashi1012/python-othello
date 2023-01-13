import pytest
from board import Board

board = Board()

def test_playable():
    assert board.playable() == [(2, 3), (3, 2), (4, 5), (5, 4)]