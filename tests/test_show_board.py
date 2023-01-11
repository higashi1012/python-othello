import pytest
from othello import show_board


def test_show_board():

    board = [['□']*8 for _ in range(8)]
    assert show_board('◎', '●', board) == None

def test_show_board_invalid_params():
    with pytest.raises(TypeError):
        show_board(120, 'hoge', 201)

    with pytest.raises(TypeError):
        show_board('hoge', 'fuga', 'piyo')

    with pytest.raises(TypeError):
        show_board(123, 456, 789)