# dp

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix) for i in range(len(matrix))]
        for i in range(len(matrix)):
            dp[0][i] = matrix[0][i]

        for i in range(1, len(matrix)):
            for j in range(0, len(matrix)):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == len(matrix)-1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1]) + matrix[i][j]
        return min(dp[-1])

# update dp 

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = matrix
        for i in range(1, n):
            for j in range(n):
                left, top, right = max(j-1, 0), j, min(j+1, n-1)
                dp[i][j] += min(dp[i-1][left], dp[i-1][top], dp[i-1][right])
        return min(dp[n-1])