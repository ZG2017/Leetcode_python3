# dp with cache to save space
# first, run dp, dp[i][j] represents the max height of the rectangle ending at (i,j)
# then, for each (i,j), calculate the max rectangle size by iterating over the width

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])

        if n == 1 and m == 1:
            return int(matrix[0][0])

        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1 if matrix[0][i] == '1' else 0
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == '0':
                    continue
                    dp[i][j] == 0
                else:
                    if matrix[i-1][j] == '0':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i-1][j]
        
        max_size = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    continue
                if matrix[i][j] == '1':
                    cur_max_height = dp[i][j]
                    cur_max_size = 0
                    for z in range(j+1):
                        if dp[i][j-z] == 0:
                            break
                        cur_max_height = min(cur_max_height, dp[i][j-z])
                        cur_max_size = cur_max_height * (z + 1)
                        max_size = max(max_size, cur_max_size)
        return max_size


