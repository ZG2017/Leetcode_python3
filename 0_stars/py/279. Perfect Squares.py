# mine:
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        self.res = float("inf")
        def helper(n,counter):
            if n < 0 or counter > self.res:
                return
            elif n == 0:
                self.res = counter
                return
            tmp = int(n**0.5)
            for i in reversed(range(1,tmp+1)):
                if i**2 * (self.res-counter) < n:
                    break
                helper(n-i**2,counter+1)
        helper(n,0)
        return self.res
