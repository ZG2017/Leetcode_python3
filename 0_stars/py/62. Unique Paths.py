# mine_1: (permutation)
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """  
        a = m+n-1-1
        counter_1 = n-1
        tmp_1 = 1
        tmp_2 = 1
        for i in range(1,n):
            tmp_1 *= a
            tmp_2 *= i
            a -= 1
        return int(tmp_1/tmp_2)


# mine_2:(dfs/recursion)(TLE)
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.res = 0
        def dfs(ri,ci):
            if ri == n-1:
                self.res += 1
                return 
            if ci == m-1:
                self.res += 1
                return
            dfs(ri+1,ci)
            dfs(ri,ci+1)
        dfs(0,0)
        return self.res

# updated: (dp)
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        board = [[1]*m for _ in range(n)] 
        for i in range(1,n):
            for j in range(1,m):
                board[i][j] = board[i-1][j] + board[i][j-1]
        return board[n-1][m-1]
