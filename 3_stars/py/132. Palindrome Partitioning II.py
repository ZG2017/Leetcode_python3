# updated: (MLE)(dp)
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(s)
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                dp[i] = 0
            else:
                flag = True
                for j in range(1,i):
                    if s[j:i+1] == s[j:i+1][::-1]:
                        if flag:
                            dp[i] = min(dp[i-1]+1,dp[j-1]+1)
                            flag = False
                        else:
                            dp[i] = min(dp[i],dp[j-1]+1)
                if flag:
                    dp[i] = dp[i-1]+1
        return dp[-1]



# updated:(dp)
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [0 for __ in range(n)]
        isPal = [[False for __ in range(n)] for __ in range(n)]
        for i in range(n):
            m = i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
                    m = 0 if j == 0 else min(m, dp[j - 1] + 1)
            dp[i] = m
        return dp[-1]


# updated:(dp, but much faster)
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # acceleration
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # algorithm
        cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            # even palindrome
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]

