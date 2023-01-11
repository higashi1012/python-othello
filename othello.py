SPACE = '□'
WHITE = '◎'
BLACK = '●'
DIRECTION_xy = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)

board = [[SPACE]*8 for _ in range(8)]
board[3][3], board[3][4] = WHITE, BLACK
board[4][3], board[4][4] = BLACK, WHITE
player = BLACK
opponent = WHITE

def turn():
    global player, opponent
    player, opponent = opponent, player

def count(piece: str, board: list):
    if not (isinstance(piece, str) and isinstance(board, list)):
        raise TypeError()
    return sum(cell == piece for row in board for cell in row)

def show_board(WHITE, BLACK, board):
    print('YX1 2 3 4 5 6 7 8')
    for y, row in enumerate(board, 1):
        print(y, *row)
    white = count(WHITE, board)
    black = count(BLACK, board)
    print(f'{BLACK}:{black} vs {WHITE}:{white}'.rjust(17))

def reversible_places(x, y, dx, dy, piece: str, SPACE: str):
    if not (isinstance(piece, str) and isinstance(SPACE, str)):
        raise TypeError()
    places = []
    x, y = x + dx, y + dy
    while 0 <= x < 8 and 0 <= y < 8 and board[y][x] != SPACE:
        if board[y][x] == piece:
            return places
        places.append((x, y))
        x, y = x + dx, y + dy
    return []

def putable_places(piece, SPACE, DIRECTION_xy, board):
    return [(x, y) for x in range(8) for y in range(8)
            if board[y][x] == SPACE
            if any(reversible_places(x, y, dx, dy, piece, SPACE)
                for dx, dy in DIRECTION_xy)]

def playable(SPACE, DIRECTION_xy, board):
    return putable_places(BLACK, SPACE, DIRECTION_xy, board) or putable_places(WHITE, SPACE, DIRECTION_xy, board)

def put_and_reverse(x, y, player, SPACE, DIRECTION_xy, board):
    board[y][x] = player
    for dx, dy in DIRECTION_xy:
        for rx, ry in reversible_places(x, y, dx, dy, player, SPACE):
            board[ry][rx] = player

def choose_place(request):
    while True:
        place = input(request)
        if place.isdigit() and 1 <= int(place) <= 8:
            return int(place)
        print('1〜8 の数字を入力してください')

def show_result(WHITE, BLACK, board):
    white = count(WHITE, board)
    black = count(BLACK, board)
    if black > white:
        judge = f'{BLACK}の勝ち'
    elif white > black:
        judge = f'{WHITE}の勝ち'
    else:
        judge = '引き分け'
    print(f'{judge}です。お疲れさまでした。')

def play():
    while playable(SPACE, DIRECTION_xy, board):
        show_board(WHITE, BLACK, board)
        putable_places_ = putable_places(player, SPACE, DIRECTION_xy, board)
        if not putable_places_:
            print(f'{player}は置ける場所がありません。パスします。')
            turn()
            putable_places_ = putable_places(player, SPACE, DIRECTION_xy, board)
        print(f'{player}の番です。')
        print('置ける場所(X,Y)は', *[(x+1,y+1) for x, y in putable_places_], 'です。')
        x = choose_place('X座標を入力してください。') - 1
        y = choose_place('Y座標を入力してください。') - 1
        if (x, y) in putable_places_:
            put_and_reverse(x, y, player, SPACE, DIRECTION_xy, board)
            turn()
        else:
            print('その場所には置けません。')
    show_board(WHITE, BLACK, board)
    show_result(WHITE, BLACK, board)


if __name__ == '__main__':
    play()