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
    
def count(piece):
    return sum(cell == piece for row in board for cell in row)

def show_board():
    print('YX1 2 3 4 5 6 7 8')
    for y, row in enumerate(board, 1):
        print(y, *row)
    white = count(WHITE)
    black = count(BLACK)
    print(f'{BLACK}:{black} vs {WHITE}:{white}'.rjust(17))
    
def reversible_places(x, y, dx, dy, piece):
    places = []
    x, y = x + dx, y + dy
    while 0 <= x < 8 and 0 <= y < 8 and board[y][x] != SPACE:
        if board[y][x] == piece:
            return places
        places.append((x, y))
        x, y = x + dx, y + dy
    return []

def putable_places(piece):
    return [(x, y) for x in range(8) for y in range(8)
            if board[y][x] == SPACE
            if any(reversible_places(x, y, dx, dy, piece)
                for dx, dy in DIRECTION_xy)]

def playable():
    return putable_places(BLACK) or putable_places(WHITE)

def put_and_reverse(x, y):
    board[y][x] = player
    for dx, dy in DIRECTION_xy:
        for rx, ry in reversible_places(x, y, dx, dy, player):
            board[ry][rx] = player

def choose_place(request):
    while True:
        place = input(request)
        if place.isdigit() and 1 <= int(place) <= 8:
            return int(place)
        print('1〜8 の数字を入力してください')

def show_result():
    white = count(WHITE)
    black = count(BLACK)
    if black > white:
        judge = f'{BLACK}の勝ち'
    elif white > black:
        judge = f'{WHITE}の勝ち'
    else:
        judge = '引き分け'
    print(f'{judge}です。お疲れさまでした。')

def play():
    while playable():
        show_board()
        putable_places_ = putable_places(player)
        if not putable_places_:
            print(f'{player}は置ける場所がありません。パスします。')
            turn()
            putable_places_ = putable_places(player)
        print(f'{player}の番です。')
        print('置ける場所(X,Y)は', *[(x+1,y+1) for x, y in putable_places_], 'です。')
        x = choose_place('X座標を入力してください。') - 1
        y = choose_place('Y座標を入力してください。') - 1
        if (x, y) in putable_places_:
            put_and_reverse(x, y)
            turn()
        else:
            print('その場所には置けません。')
    show_board()
    show_result()


if __name__ == '__main__':
    play()