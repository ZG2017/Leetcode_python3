# mine:
from gettext import dpgettext


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = grid[0][0]
        """
        for i in range(1,m):
            dp[0][i] = grid[i]+dp[]
            """
            
        for i in range(n):
            for j in range(m):
                if not i and not j:
                    dp[i][j] = grid[0][0]
                elif not i:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif not j:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j])+ grid[i][j]
        return dp[n-1][m-1]

# update dp

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        tmp = 0
        if m == 1 or n == 1:
            for i in range(m):
                for j in range(n):
                    tmp += grid[i][j]
        
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif 0 <= i-1 and j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif 0 <= j-1 and i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
