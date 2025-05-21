# mine: dp
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*(len(s)+1)
        if s[0] == "0":
            return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(1,len(s)):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i+1] = dp[i-1]
                else:
                    dp[i+1] = 0
            elif int(s[i])<=6 and int(s[i])>0:
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i+1] = dp[i]+dp[i-1]
                else:
                    dp[i+1] = dp[i]
            else:
                if s[i-1] == "1":
                    dp[i+1] = dp[i]+dp[i-1]
                else:
                    dp[i+1] = dp[i]
        return dp[len(s)]
