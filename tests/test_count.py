import pytest
from board import Board

board = Board()

def test_count():
    assert board.count('□') == 60
    assert board.count('●') == 2
    assert board.count('◎') == 2

def test_count_invalid_params():
    with pytest.raises(TypeError):
        board.count(120)

    with pytest.raises(TypeError):
        board.count([123])
