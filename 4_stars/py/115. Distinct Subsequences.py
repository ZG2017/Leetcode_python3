# updated:(dp)
class Solution:
    def numDistinct(self, s, t):
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1,len(t)+1):
            for j in range(i,len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[j][i] = dp[j-1][i-1] + dp[j-1][i]
                else:
                    dp[j][i] = dp[j-1][i]
        return dp[-1][-1]
