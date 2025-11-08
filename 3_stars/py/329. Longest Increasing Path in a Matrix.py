# mine:(naive DFS, TLE)
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        self.res = 1
        n = len(matrix)
        m = len(matrix[0])
        def helper(path,lens):
            if path[-1][0]-1 >= 0 and matrix[path[-1][0]-1][path[-1][1]] > matrix[path[-1][0]][path[-1][1]]:
                helper(path+[(path[-1][0]-1,path[-1][1])],lens+1)
            if path[-1][0]+1 < n and matrix[path[-1][0]+1][path[-1][1]] > matrix[path[-1][0]][path[-1][1]]:
                helper(path+[(path[-1][0]+1,path[-1][1])],lens+1)
            if path[-1][1]-1 >= 0 and matrix[path[-1][0]][path[-1][1]-1] > matrix[path[-1][0]][path[-1][1]]:
                helper(path+[(path[-1][0],path[-1][1]-1)],lens+1)
            if path[-1][1]+1 < m and matrix[path[-1][0]][path[-1][1]+1] > matrix[path[-1][0]][path[-1][1]]:
                helper(path+[(path[-1][0],path[-1][1]+1)],lens+1)
            self.res = max(self.res,lens)
        for i in range(n):
            for j in range(m):
                helper([(i,j)],1)
        return self.res



# mine:(updated DFS)
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        self.res = 1
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                matrix[i][j] = [matrix[i][j],-1]
        def helper(i,j):
            tmp_1,tmp_2,tmp_3,tmp_4 = 0,0,0,0
            if i-1 >= 0 and matrix[i-1][j][0] > matrix[i][j][0]:
                tmp_1 = helper(i-1,j) if matrix[i-1][j][1] == -1 else matrix[i-1][j][1]
            if i+1 < n and matrix[i+1][j][0] > matrix[i][j][0]:
                tmp_2 = helper(i+1,j) if matrix[i+1][j][1] == -1 else matrix[i+1][j][1]
            if j-1 >= 0 and matrix[i][j-1][0] > matrix[i][j][0]:
                tmp_3 = helper(i,j-1) if matrix[i][j-1][1] == -1 else matrix[i][j-1][1]
            if j+1 < m and matrix[i][j+1][0] > matrix[i][j][0]:
                tmp_4 = helper(i,j+1) if matrix[i][j+1][1] == -1 else matrix[i][j+1][1]
            matrix[i][j][1] = max(tmp_1,tmp_2,tmp_3,tmp_4) + 1
            return matrix[i][j][1]
        for i in range(n):
            for j in range(m):
                if matrix[i][j][1] == -1:
                    self.res = max(helper(i,j),self.res)
        return self.res


# sort + dp

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        holder = []
        for i in range(m):
            for j in range(n):
                holder.append((matrix[i][j], i, j))
        
        sorted_holder = sorted(holder, key=lambda x:x[0])
        
        overall_max = 0
        dp = [[1] * n for _ in range(m)]
        for v, i, j in sorted_holder:
            cur_max = 0
            if i + 1 < m and matrix[i][j] > matrix[i+1][j]:
                cur_max = max(cur_max, dp[i+1][j])
            if j + 1 < n and matrix[i][j] > matrix[i][j+1]:
                cur_max = max(cur_max, dp[i][j+1])
            if i - 1 >= 0 and matrix[i][j] > matrix[i-1][j]:
                cur_max = max(cur_max, dp[i-1][j])
            if j - 1 >= 0 and matrix[i][j] > matrix[i][j-1]:
                cur_max = max(cur_max, dp[i][j-1])
            dp[i][j] = cur_max + 1
            overall_max = max(overall_max, dp[i][j])
        return overall_max