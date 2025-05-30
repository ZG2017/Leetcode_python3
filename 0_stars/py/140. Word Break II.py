# mine:（TLE）
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        def helper(strs,tmp,lens):
            if lens == len(s):
                res.append(tmp[:-1])
            for word in wordDict:
                n = len(word)
                if strs[:n] == word:
                    helper(strs[n:],tmp+strs[:n]+" ",lens+n)
                else:
                    continue
        helper(s,"",0)
        return res 
