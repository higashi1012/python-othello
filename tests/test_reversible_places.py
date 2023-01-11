import pytest
from othello import reversible_places

SPACE = '□'
WHITE = '◎'
BLACK = '●'
DIRECTION_xy = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
board = [[SPACE]*8 for _ in range(8)]
board[3][3], board[3][4] = WHITE, BLACK
board[4][3], board[4][4] = BLACK, WHITE

def test_reversible_places():
    assert reversible_places(2, 3, 1, 0, BLACK, SPACE) == [(3, 3)]
    assert reversible_places(2, 3, 1, 0, WHITE, SPACE) == []
    assert reversible_places(2, 3, 1, 1, BLACK, SPACE) == []
    assert reversible_places(5, 3, -1, 0, WHITE, SPACE) == [(4, 3)]

def test_reversible_places_invalid_params():
    with pytest.raises(TypeError):
        reversible_places([3],'hoge', [7], 120, 'huga')

    with pytest.raises(TypeError):
        reversible_places(1, 2, 3, 4, 5, 6)

    with pytest.raises(TypeError):
        reversible_places(123, 456, 7, 8, [678], 'a')
