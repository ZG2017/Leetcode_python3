# updated:
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_max_profit = 0
        n = len(prices)
        first_profits = [0] * n
        min_price = float('inf')

        for i in range(n):
            min_price = min(min_price, prices[i])
            total_max_profit = max(total_max_profit, prices[i] - min_price)
            first_profits[i] = total_max_profit

        max_profit = 0
        max_price = float('-inf')
        for i in range(n - 1, 0, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])
            total_max_profit = max(total_max_profit, max_profit + first_profits[i - 1])
        return total_max_profit



# udpated:  (dont understand!!!)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        buy1 = buy2 = -1<<31
        sell1 = sell2 = 0
        for p in prices:
            if buy1 < -p:
                buy1 = -p
            if sell1 < buy1+p:
                sell1 = buy1+p
            if buy2 < sell1-p:
                buy2 = sell1-p
            if sell2 < buy2+p:
                sell2 = buy2+p

            # print(buy1, sell1, buy2, sell2)

        return sell2

