
class Board:

    def __init__(self):
        self.SPACE = '□'
        self.WHITE = '◎'
        self.BLACK = '●'
        self.DIRECTION_xy = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
        self.values = [['□'] * 8 for _ in range(8)]
        self.values[3][3], self.values[3][4] = self.WHITE, self.BLACK
        self.values[4][3], self.values[4][4] = self.BLACK, self.WHITE

    def count(self, piece: str) -> int:
        if not isinstance(piece, str):
            raise TypeError(f"The argument 'peice' must be string. But actual: {type(piece)}")
        return sum(cell == piece for row in self.values for cell in row)


    def reversible_places(self, x, y, dx, dy, piece: str) -> list:
        if not isinstance(piece, str):
            raise TypeError(f"The argument 'peice' must be string. But actual: {type(piece)}")
        places = []
        x, y = x + dx, y + dy
        while 0 <= x < 8 and 0 <= y < 8 and self.values[y][x] != self.SPACE:
            if self.values[y][x] == piece:
                return places
            places.append((x, y))
            x, y = x + dx, y + dy
        return []

    def putable_places(self, piece) -> list:
        return [(x, y) for x in range(8) for y in range(8)
                if self.values[y][x] == self.SPACE
                if any(self.reversible_places(x, y, dx, dy, piece)
                    for dx, dy in self.DIRECTION_xy)]

    def playable(self) -> list:
        return self.putable_places(self.BLACK) or self.putable_places(self.WHITE)

    def put_and_reverse(self, x, y, player):
        self.values[y][x] = player
        for dx, dy in self.DIRECTION_xy:
            for rx, ry in self.reversible_places(x, y, dx, dy, player):
                self.values[ry][rx] = player



