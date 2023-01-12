
class Othello():

    SPACE = '□'
    WHITE = '◎'
    BLACK = '●'
    DIRECTION_xy = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)

    def __init__(self):
        self.board = [[self.SPACE] * 8 for _ in range(8)]
        self.board[3][3], self.board[3][4] = self.WHITE, self.BLACK
        self.board[4][3], self.board[4][4] = self.BLACK, self.WHITE
        self.player, self.opponent = self.BLACK, self.WHITE

    def count(self, piece: str) -> int:
        if not isinstance(piece, str):
            raise TypeError(f"The argument 'peice' must be string. But actual: {type(piece)}")
        return sum(cell == piece for row in self.board for cell in row)

    def show_board(self):
        print('YX1 2 3 4 5 6 7 8')
        for y, row in enumerate(self.board, 1):
            print(y, *row)
        white = self.count(self.WHITE)
        black = self.count(self.BLACK)
        print(f'{self.BLACK}:{black} vs {self.WHITE}:{white}'.rjust(17))

    def reversible_places(self, x, y, dx, dy, piece: str) -> list:
        if not isinstance(piece, str):
            raise TypeError(f"The argument 'peice' must be string. But actual: {type(piece)}")
        places = []
        x, y = x + dx, y + dy
        while 0 <= x < 8 and 0 <= y < 8 and self.board[y][x] != self.SPACE:
            if self.board[y][x] == piece:
                return places
            places.append((x, y))
            x, y = x + dx, y + dy
        return []

    def putable_places(self, piece) -> list:
        return [(x, y) for x in range(8) for y in range(8)
                if self.board[y][x] == self.SPACE
                if any(self.reversible_places(x, y, dx, dy, piece)
                    for dx, dy in self.DIRECTION_xy)]

    def playable(self) -> list:
        return self.putable_places(self.BLACK) or self.putable_places(self.WHITE)

    def put_and_reverse(self, x, y, player):
        self.board[y][x] = player
        for dx, dy in self.DIRECTION_xy:
            for rx, ry in self.reversible_places(x, y, dx, dy, player):
                self.board[ry][rx] = player

    def choose_place(self, request):
        while True:
            place = input(request)
            if place.isdigit() and 1 <= int(place) <= 8:
                return int(place)
            print('1〜8 の数字を入力してください')

    def show_result(self):
        white = self.count(self.WHITE)
        black = self.count(self.BLACK)
        if black > white:
            judge = f'{self.BLACK}の勝ち'
        elif white > black:
            judge = f'{self.WHITE}の勝ち'
        else:
            judge = '引き分け'
        print(f'{judge}です。お疲れさまでした。')

    def play(self):
        while self.playable():
            self.show_board()
            putable_places_ = self.putable_places(self.player)
            if not putable_places_:
                print(f'{self.player}は置ける場所がありません。パスします。')
                self.player, self.opponent = self.opponent, self.player
                putable_places_ = self.putable_places(self.player)
            print(f'{self.player}の番です。')
            print('置ける場所(X,Y)は', *[(x+1,y+1) for x, y in putable_places_], 'です。')
            x = self.choose_place('X座標を入力してください。') - 1
            y = self.choose_place('Y座標を入力してください。') - 1
            if (x, y) in putable_places_:
                self.put_and_reverse(x, y, self.player)
                self.player, self.opponent = self.opponent, self.player
            else:
                print('その場所には置けません。')
        self.show_board()
        self.show_result()


if __name__ == '__main__':
    Othello().play()
