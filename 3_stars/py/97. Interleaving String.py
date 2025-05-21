# mine:recursion(TLE)
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 == "" or s2 == "":
            if (s1 == "" and s2 == "" and s3 == "")\
            or (s1 == "" and s2 == s3)\
            or (s2 == "" and s1 == s3):
                return True
            else:
                return False
                
        
        if (s1[0] == s3[0] and self.isInterleave(s1[1:],s2,s3[1:]))\
        or (s2[0] == s3[0] and self.isInterleave(s1,s2[1:],s3[1:])):
            return True
        else:
            return False


# mine:dp
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        
        for i in range(1,m+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True 
            else: 
                break
        for i in range(1,n+1):
            if s2[:i] == s3[:i]:
                dp[0][i] = True
            else: 
                break
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s3[i+j-1]:
                    if dp[i-1][j] == True:
                        dp[i][j] = True
                if s2[j-1] == s3[i+j-1]:
                    if dp[i][j-1] == True:
                        dp[i][j] = True
        return dp[m][n]
