# my:
# import numpy as np
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        tmp = (numRows - 1)*2
        base = int(len(s)/tmp)
        if base == 0:
            if int(len(s)/numRows) == 0:
                x = 1
            else:
                x = 1 + len(s)%numRows
        else:    
            remain = len(s)%tmp
            if remain == 0:
                x = base*(numRows-1)
            else:
                remain2 = int(remain/numRows)
                if remain2 == 0:
                    x = base*(numRows-1) + 1
                else:
                    x = base*(numRows-1) + 1 + remain%numRows
        
        savemat = np.zeros((numRows, x),dtype = str)
        i = 0
        j = 0
        going_down = True
        for k in s:
            savemat[i][j] = k
            if going_down:
                i+=1
            else:
                i-=1
                j+=1
            if i == numRows - 1:
                going_down = False
            if i == 0:
                going_down = True
        
        return ''.join(savemat.flatten().tolist())
            

# updated:
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows

        index, step = 0, 1

        for c in s:
            result[index] += c
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step

        return ''.join(result)

