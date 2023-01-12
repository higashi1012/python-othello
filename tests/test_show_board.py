import pytest
from othello import Othello


def test_show_board():

    assert Othello().show_board() == None