# dp (0-1 knapsack problem)
# for each string, we can either include it or not include it.
# m and n are maxiumn compacity of 0s and 1s respectively.
# weights are 1 for each string.
# number of 0 and 1 in each string are the values of the items.
# dp[i][j] means the maximum number of strings that can be formed with i 0s and j 1s

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        data = [{0:str_.count('0'), 1:str_.count('1')} for str_ in strs]

        dp = [[0]*(m+1) for _ in range(n+1)]

        dp[0][0] = 0

        for d in data:
            for i in range(n, d[1]-1, -1):
                for j in range(m, d[0]-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-d[1]][j-d[0]]+1)
        return dp[n][m]