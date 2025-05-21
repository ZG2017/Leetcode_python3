# mine:
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minp = prices[0]
        maxp = 0
        for i in prices:
            if i < minp:
                minp = i
            if i-minp > maxp:
                maxp = i-minp
        return maxp

