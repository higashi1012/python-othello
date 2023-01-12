import pytest
from othello import Othello

def test_show_board():
    board = [['□']*8 for _ in range(8)]
    assert Othello().show_board() == None
