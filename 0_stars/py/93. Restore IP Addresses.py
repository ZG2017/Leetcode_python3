# mine:
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def helper(s,n,tmp):
            if n == 1:
                if len(s) >= 2 and s[0] == "0":
                    return
                elif int(s) <= 255 and int(s) >= 0:
                    res.append(tmp+s)
                else:
                    return
            for i in range(1,4):
                if s[i:] != "":
                    if len(s[:i]) >=2 and s[:i][0] == "0":
                        continue                        
                    elif int(s[:i]) <= 255 and int(s[:i]) >= 0:
                        helper(s[i:],n-1,tmp+s[:i]+".")
                else:
                    break
        helper(s,4,"")
        return res 