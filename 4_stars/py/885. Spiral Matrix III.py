# # useful patterns that make code concise:
# 1. 90 deg Clockwise can be controlled as: diri, dirj = dirj, -diri.
# 2. after change direction twice, the length of walking over next direction will be added by 1.

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i,j = rStart, cStart

        diri, dirj = 0, 1 # directions to move
        twice = 2
        res = []
        moves = 1
        next_moves = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and ( -1 < j < cols):
                res.append([i,j])

            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri # 90 deg Clockwise
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res

