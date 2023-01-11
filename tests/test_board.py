import pytest
from othello import show_board

board = [['□']*8 for _ in range(8)]

def test_show_board():
    board = [['□']*8 for _ in range(8)]
    assert show_board('WHITE', 'BLACK', board) == None

def test_show_board_invalid_params():
    with pytest.raises(TypeError):
        show_board(120, 'hoge', board)
