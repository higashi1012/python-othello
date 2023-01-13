import pytest
from io import StringIO
from view import View
from board import Board

board = Board()
view = View(board)

def test_choose_place(monkeypatch):
    number_inputs = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert view.choose_place('X座標を入力してください。') == 1

    number_inputs = StringIO('0\na\n8\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert view.choose_place('X座標を入力してください。') == 8

    number_inputs = StringIO('9\n1\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert view.choose_place('X座標を入力してください。') == 1

    number_inputs = StringIO('200\n11\n189\n5')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert view.choose_place('X座標を入力してください。') == 5
