# mine:
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        elif not t:
            return False
        pt = 0
        ps = 0
        while pt < len(t):
            if t[pt] == s[ps]:
                pt += 1
                ps += 1
            else:
                pt += 1
                continue
            if ps == len(s):
                return True
        return False
        

# updated: (use .find of String)
class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        for char in s:
            idx = t.find(char)
            if idx < 0:
                return False
            t = t[idx + 1:]
        
        return True
