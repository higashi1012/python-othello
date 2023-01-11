import pytest
from othello import count


def test_count():
    piece = 'BLACK'
    board = [['BLACK', 'BLACK', 'WHITE', 'BLACK']]
    assert count(piece, board) == 3
    assert count(
        'hoge',
        [['hoge']]
    ) == 1


def test_count_invalid_params():
    with pytest.raises(TypeError):
        count(120, 'hoge')

    with pytest.raises(TypeError):
        count('hoge', 'fuga')
