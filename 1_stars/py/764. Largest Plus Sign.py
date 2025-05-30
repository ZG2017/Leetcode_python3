class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        r, c = n+2, n+2
        holder = [[[0]*4 for _ in range(c)] for _ in range(r)]
        mines = set([(i[0]+1, i[1]+1) for i in mines])
        for i in range(1, r-1):
            for j in range(1, c-1):
                if (i, j) not in mines:
                    holder[i][j][0] = holder[i-1][j][0] + 1
                    holder[i][j][1] = holder[i][j-1][1] + 1
        res = 0
        for i in range(r-2, 0, -1):
            for j in range(c-2, 0, -1):
                if (i, j) not in mines:
                    holder[i][j][2] = holder[i+1][j][2] + 1
                    holder[i][j][3] = holder[i][j+1][3] + 1

                if min(holder[i][j]) > res:
                    res = min(holder[i][j])
        return res 