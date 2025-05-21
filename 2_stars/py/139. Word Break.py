# mine:(TLE)
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def helper(strs):
            if strs in wordDict:
                return True
            for i in range(1,len(strs)):
                if strs[:i] in wordDict:
                    if helper(strs[i:]):
                        return True
                else:
                    continue
            return False
        return helper(s)



# updated:(dp)
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
