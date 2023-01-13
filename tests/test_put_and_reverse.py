import pytest
from board import Board

board = Board()

def test_put_and_reversee():
    assert board.put_and_reverse(3, 2, '●') == None