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

# dp with "*" merging
# dp[i][j] means whether the first i characters of s match the first j characters of p
# if p[j] == '*', then dp[i][j] = any([dp[x][j-1] for x in range(0, i+1)]) (early stopping if found one True)
# if p[j] == '?', then dp[i][j] = dp[i-1][j-1]
# if p[j] == s[i], then dp[i][j] = dp[i-1][j-1]
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        new_p = []
        for i in p:
            if i == '*' and new_p and new_p[-1] == '*':
                continue
            else:
                new_p.append(i)
        p = ''.join(new_p)

        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0] = True
        for i in range(1, n+1):
            dp[0][i] = all([j == '*' for j in p[:i]])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    for x in range(0, i+1):
                        if dp[x][j-1]:
                            dp[i][j] = True
                            break
        return dp[m][n]


# update: dp[i][j] = dp[i-1][j] or dp[i][j-1] if p[j-1] == '*'
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        new_p = []
        for i in p:
            if i == '*' and new_p and new_p[-1] == '*':
                continue
            else:
                new_p.append(i)
        p = ''.join(new_p)

        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0] = True
        for i in range(1, n+1):
            dp[0][i] = all([j == '*' for j in p[:i]])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[m][n]


