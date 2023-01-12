import pytest
from othello import Othello

def test_playable():
    assert Othello().playable() == [(2, 3), (3, 2), (4, 5), (5, 4)]