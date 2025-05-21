# updated:  (dp)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        sell = [0 for _ in range(len(prices))]
        buy = [0 for _ in range(len(prices))]
        sell[0] = 0
        sell[1] = max(0,prices[1] - prices[0])
        buy[0] = -prices[0]
        buy[1] = -prices[1]
        for i in range(2,len(prices)):
            dltea = prices[i]-prices[i-1]
            sell[i] = max(sell[i-1] + dltea, buy[i-1] + prices[i])
            buy[i] = max(sell[i-2] - prices[i], buy[i-1] - dltea)
        return max(sell)



# updated:
class Solution:
  def maxProfit(self, prices):
    buy = -float('inf')
    sell = wait = 0
    for p in prices:
      buy, sell, wait = max(wait - p, buy), max(buy + p, sell), max(sell, wait)
      
    return max(buy, sell, wait)

