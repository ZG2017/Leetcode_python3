# mine:
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        tmp = []
        for _ in range(rowIndex):
            tmp = [1]
            for i in range(len(res)-1):
                tmp.append(res[i]+res[i+1])
            tmp.append(1)
            res = tmp
        return res
