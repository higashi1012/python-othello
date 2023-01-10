from othello import turn, show_board, reversible_places, count, putable_places, playable, put_and_reverse, choose_place, show_result, play

SPACE = '□'
WHITE = '◎'
BLACK = '●'
DIRECTION_xy = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)

board = [[SPACE]*8 for _ in range(8)]
board[3][3], board[3][4] = WHITE, BLACK
board[4][3], board[4][4] = BLACK, WHITE
player = BLACK
opponent = WHITE

def test_playable():
    return putable_places(BLACK) or putable_places(WHITE)