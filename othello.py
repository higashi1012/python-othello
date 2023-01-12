from board import Board
from view import View

def play():
    board = Board()
    view = View(board)
    player, opponent = board.BLACK, board.WHITE
    while board.playable():
        view.show_board()
        putable_places_ = board.putable_places(player)
        if not putable_places_:
            print(f'{player}は置ける場所がありません。パスします。')
            player, opponent = opponent, player
            putable_places_ = board.putable_places(player)
        print(f'{player}の番です。')
        print('置ける場所(X,Y)は', *[(x+1,y+1) for x, y in putable_places_], 'です。')
        x = view.choose_place('X座標を入力してください。') - 1
        y = view.choose_place('Y座標を入力してください。') - 1
        if (x, y) in putable_places_:
            board.put_and_reverse(x, y, player)
            player, opponent = opponent, player
        else:
            print('その場所には置けません。')
    view.show_board()
    view.show_result()

if __name__ == '__main__':
    play()
