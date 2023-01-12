import pytest
from othello import Othello

def test_reversible_places():
    assert Othello().reversible_places(2, 3, 1, 0, '●') == [(3, 3)]
    assert Othello().reversible_places(2, 3, 1, 0, '◎') == []
    assert Othello().reversible_places(2, 3, 1, 1, '●') == []
    assert Othello().reversible_places(5, 3, -1, 0, '◎') == [(4, 3)]

def test_reversible_places_invalid_params():
    with pytest.raises(TypeError):
        Othello().reversible_places([3],'hoge', [7], 120, 'huga')

    with pytest.raises(TypeError):
        Othello().reversible_places(1, 2, 3, 4, 5)

    with pytest.raises(TypeError):
        Othello().reversible_places(123, 456, 7, 8, [678])
