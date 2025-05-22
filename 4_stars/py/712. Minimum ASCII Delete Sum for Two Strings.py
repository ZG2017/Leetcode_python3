# dynamic programming: modified based on Longest Common Subsequence 
# refer: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solutions/6736689/conquer-minimum-ascii-delete-sum-for-two-strings-with-smart-dp-beats-100/?envType=problem-list-v2&envId=dynamic-programming
# key notes:
# 1. dp[i][j] is the minimum ASCII delete sum of s1[0:i] and s2[0:j]
# if s[i]==s[j], dp[i][j]=dp[i-1][j-1], no need to delete any char
# if s[i]!=s[j], dp[i][j]=min(dp[i-1][j]+s1[i], dp[i][j-1]+s2[j]), delete one char from s1 or s2 and compare the cost of deleting the char  

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        return dp[m][n]