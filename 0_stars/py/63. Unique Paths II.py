# mine:
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[n-1][m-1] == 1:
            return 0
        dp = [[1]*(m) for _ in range(n)]
        flag = False
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                flag = True
            if flag:
                dp[0][i] = 0
        flag = False
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                flag = True
            if flag:
                dp[i][0] = 0
                
        for i in range(1,n):
            for j in range(1,m):   
                if obstacleGrid[i-1][j] and not obstacleGrid[i][j-1]:
                    dp[i][j] = dp[i][j-1]
                elif not obstacleGrid[i-1][j] and obstacleGrid[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                elif obstacleGrid[i-1][j] and obstacleGrid[i][j-1]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n-1][m-1]
