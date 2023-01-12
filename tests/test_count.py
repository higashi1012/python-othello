import pytest
from othello import Othello


def test_count():
    assert Othello().count('□') == 60
    assert Othello().count('●') == 2
    assert Othello().count('◎') == 2

def test_count_invalid_params():
    with pytest.raises(TypeError):
        Othello().count(120)

    with pytest.raises(TypeError):
        Othello().count([123])
