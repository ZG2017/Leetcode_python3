# Tic Tac Toe solution
class Solution:
    def is_win(self, moves):
        if len(moves) <= 2:
            return False
        if ((0,0) in moves and (1,1) in moves and (2,2) in moves) or \
            ((0,2) in moves and (1,1) in moves and (2,0) in moves):
            return True
        xs, ys = zip(*moves)
        xc = Counter(xs)
        yc = Counter(ys)
        if any(v >= 3 for v in xc.values()) or any(v >= 3 for v in yc.values()):
            return True
        else:
            return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        from collections import Counter
        As = [(x,y) for x, y in moves[::2]]
        Bs = [(x,y) for x, y in moves[1::2]]
        if self.is_win(As):
            return 'A'
        elif self.is_win(Bs):
            return 'B'
        elif len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending' 