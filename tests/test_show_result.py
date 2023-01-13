import pytest
from view import View
from board import Board

board = Board()
view = View(board)

def test_show_result():
    assert View(board).show_result() == None