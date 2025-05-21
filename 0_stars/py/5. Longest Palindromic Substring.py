# import numpy as np
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        maxi = 0
        place = 0
        rev = s[::-1]
        p = 0
        record = np.zeros((len(s)+1,len(s)+1),dtype = np.int)
        for i in range(len(s)):
            for j in range(len(s)):
                if rev[j] == s[i]:
                    record[i+1][j+1] = record[i][j] + 1
                #print(rev[j+1-record[i+1][j+1]:j+1])
                #print(s[-(j+1+1):-(j+1-record[i+1][j+1]+1)])
                if record[i+1][j+1] > maxi and len(s)-j-1 == i+1-record[i+1][j+1]:
                    maxi = record[i+1][j+1]
                    p = i + 1
        
        return s[p-maxi:p]   
