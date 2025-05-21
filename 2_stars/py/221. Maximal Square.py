# mine: dp
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        maxa = 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if matrix[i][0] == "1":
                dp[i][0] = 1 
                maxa = 1
        for i in range(m):
            if matrix[0][i] == "1":
                dp[0][i] = 1 
                maxa = 1
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    tmp = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    dp[i][j] = int((tmp**0.5+1)**2)
                    if dp[i][j] > maxa:
                        maxa = dp[i][j]
        return maxa


# mine: dp faster
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        maxa = 0
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] =="1":
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxa = max(maxa,dp[i][j])
        return maxa**2
