# mine:
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices = [float("inf")]+prices+[0]
        buyp = 0 
        index = 1
        pro = 0
        while index <= len(prices)-2:
            if prices[index] <= prices[index-1] and prices[index] < prices[index+1]:
                buyp = prices[index]
                index+=1
                while prices[index] <= prices[index+1] and index <= len(prices)-2:
                    index += 1
                pro += (prices[index]-buyp)
            index += 1
        return pro


# udpated:(buy and sell and same day so that it connects lots of days)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        out = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                out += prices[i+1] - prices[i]
        return out
