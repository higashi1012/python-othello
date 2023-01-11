import pytest
from othello import playable

DIRECTION_xy = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)

def test_playable():
    assert playable('□',DIRECTION_xy, [['□']*8 for _ in range(8)]) == [(2, 3), (3, 2), (4, 5), (5, 4)]