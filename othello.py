class Othello:

    def __init__(self):
        
        self.ot_bit = list()
        for i in range(64):
            if i == 27 or i == 36:
                self.ot_bit.append('◎')
            elif i == 28 or i == 35:
                self.ot_bit.append('●')
            else:
                self.ot_bit.append('□')
        
        self.ot_offdef = '◎'
        self.ot_search = '●'
        self.ot_direction = dict()
        self.ot_direction = { 'ul' : (-1, -1),
                              'up' : ( 0, -1),
                              'ur' : (+1, -1),
                              'lt' : (-1,  0),
                              'lr' : (+1,  0),
                              'dl' : (+1, +1),
                              'dn' : (+1,  0),
                              'dr' : (+1, +1) }
        self.ot_lastposX = 0
        self.ot_lastposY = 0

    def ot_inputXY(self, otstr):
        while True:
            myXY = input(otstr)
            if myXY == '':
                continue
            if '1' <= myXY <= '8':
                return(int(myXY))