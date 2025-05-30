# brute force

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        cur_p = 1
        while cur_p <= len(s)//2:
            cur_res = s[:cur_p]
            if len(s)%len(cur_res) == 0 and cur_res*(len(s)//len(cur_res)) == s:
                return True
            cur_p += 1
        return False 