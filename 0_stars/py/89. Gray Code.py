# mine: (in binary form which is relatively slow)
from copy import deepcopy
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = [[]]
        for i in range(n):
            tmp = deepcopy(res)
            tmp = tmp[::-1]
            [j.append("1") for j in tmp]
            [j.append("0") for j in res]
            res = res+tmp
        for i in range(len(res)):
            res[i] = int("".join(res[i]),2)
        return res

# updated:(in 10_base form faster)
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        v = 1
        for i in range(1, n + 1):
            for x in reversed(res):
                res.append(v + x)
            v *= 2
        return res 