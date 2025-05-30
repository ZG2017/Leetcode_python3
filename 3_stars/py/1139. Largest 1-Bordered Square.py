# dp: https://www.youtube.com/watch?v=vi_1eHCsR9A

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0,0] for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                else:
                    if i != 0:
                        dp[i][j][0] = dp[i-1][j][0]+1
                    else:
                        dp[i][j][0] = 1
                    if j != 0:
                        dp[i][j][1] = dp[i][j-1][1]+1
                    else:
                        dp[i][j][1] = 1
        res = 0
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                cur_min = min(dp[i][j])
                if cur_min <= res:
                    continue
                for k in range(cur_min, res, -1):
                    if dp[i-k+1][j][1] >= k and dp[i][j-k+1][0] >= k:
                        res = k
                        break
        return res**2
        
