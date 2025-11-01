
# dp
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        dp = [[False]*(n) for _ in range(n)]

        max_offset = -1
        max_res = ''
        
        for offset in range(0, n):
            for i in range(0, n-offset):
                if s[i] == s[i+offset]:
                    if offset < 2:
                        dp[i][i+offset] = True
                    else:
                        dp[i][i+offset] = dp[i+1][i+offset-1]
                    if dp[i][i+offset] and offset > max_offset:
                        max_res = s[i:i+offset+1]
                        max_offset = offset
        return max_res