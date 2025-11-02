# complete knapsack problem
# dp[i] = dp[i-coin] + dp[i]
# dp[i] means the number of ways to make up amount i
# for each coin, we can either include it or not include it.

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = dp[i] + dp[i-coin]
        return dp[amount]