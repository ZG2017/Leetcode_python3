# https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-appr-5i49/
# dp with cache to save space
# the transition formula is: dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
# which represents the max square size if using dp[r][c] as the bottom right corner of the square

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side