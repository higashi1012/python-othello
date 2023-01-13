import pytest
from view import View
from board import Board

board = Board()
view = View(board)

def test_show_board():
    assert view.show_board() == None

def test_show_board_invalid_params():
    with pytest.raises(TypeError):
        view = View(3)

    with pytest.raises(TypeError):
        view = View('a')

    with pytest.raises(TypeError):
        view = View([2, 3, 4])

    with pytest.raises(Exception):
        view = View([2, 3, 4])