import pytest
from view import View
from board import Board

board = Board()
view = View(board)

def test_show_board():
    assert View(board).show_board() == None