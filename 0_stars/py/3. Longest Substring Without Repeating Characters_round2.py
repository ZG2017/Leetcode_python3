class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        res = 0
        while p2 < len(s):
            tmp = s[p2]
            while tmp in s[p1:p2]:
                p1 += 1
            if p2-p1+1 > res:
                res = p2-p1+1
            p2 += 1
        return res
        
