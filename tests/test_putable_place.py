import pytest
from othello import Othello

def test_putable_places():
    assert Othello().putable_places('●') == [(2, 3), (3, 2), (4, 5), (5, 4)]
    assert Othello().putable_places('◎') == [(2, 4), (3, 5), (4, 2), (5, 3)]