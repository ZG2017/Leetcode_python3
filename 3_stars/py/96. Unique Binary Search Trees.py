# mine:(dp)
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            tmp = 0
            for j in range(i):
                tmp += dp[j]*dp[i-j-1]
            dp[i] = tmp
        return dp[n]



# updated:(less variable, so faster)
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]*(n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j]*res[i-j-1]
        return res[n]
