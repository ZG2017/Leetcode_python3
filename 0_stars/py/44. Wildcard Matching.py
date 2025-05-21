# mine: (TLE)
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "" and p == "":
            return True
        elif s != "" and p == "":
            return False
        elif s == "" and p[0] != "*":
            return False
        elif p[0] == "*":
            j = 1
            while j < len(p) and p[j] == "*":
                j += 1
            for i in range(len(s)+1):
                if self.isMatch(s = s[i:],p = p[j:]):
                    return True
                    break
                continue
            return False
        elif (p[0] == "?" or p[0] == s[0]) and self.isMatch(s = s[1:],p = p[1:]):
            return True 
        return False

# update:
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sp = 0
        pp = 0
        last_sp = -1
        last_pp = -1
        while sp < len(s):
            if pp < len(p) and (p[pp] == "?" or p[pp] == s[sp]):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == "*":
                pp += 1
                last_sp = sp
                last_pp = pp
            elif last_pp != -1:
                last_sp += 1
                sp = last_sp
                pp = last_pp
            else:
                return False
        
        while pp < len(p) and p[pp] =="*":
            pp += 1
        
        if pp == len(p) and sp == len(s):
            return True
        else:
            return False


