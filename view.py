from board import Board

class View:

    def __init__(self, board: Board):
        if not isinstance(board, Board):
            raise TypeError(f"The argument 'board' must be Board. But actual : {type(board)}")
        self.board = board

    def show_board(self):
        print('YX1 2 3 4 5 6 7 8')
        for y, row in enumerate(self.board.values, 1):
            print(y, *row)
        white = self.board.count(self.board.WHITE)
        black = self.board.count(self.board.BLACK)
        print(f'{self.board.BLACK}:{black} vs {self.board.WHITE}:{white}'.rjust(17))

    def show_result(self):
        white = self.board.count(self.board.WHITE)
        black = self.board.count(self.board.BLACK)
        if black > white:
            judge = f'{self.board.BLACK}の勝ち'
        elif white > black:
            judge = f'{self.board.WHITE}の勝ち'
        else:
            judge = '引き分け'
        print(f'{judge}です。お疲れさまでした。')

    def choose_place(self, request):
        while True:
            place = input(request)
            if place.isdigit() and 1 <= int(place) <= 8:
                return int(place)
            print('1〜8 の数字を入力してください')