# dp (0-1 knapsack problem)
# dp[i][j] means the number of ways to achieve profit j with i people
# for each crime, we can either include it or not include it.
# n is the maximum number of people.
# time limit exceeded

class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        max_profit = sum(profit)
        dp = [[0] * (max_profit+1) for _ in range(n+1)]

        dp[0][0] = 1

        mod = 1e9+7
        for w, v in zip(group, profit):
            for i in range(n, w-1, -1):
                for j in range(max_profit, v-1, -1):
                    dp[i][j] = (dp[i][j] + dp[i-w][j-v]) % mod
        
        res = 0
        for i in range(n+1):
            for j in range(minProfit, max_profit+1):
                res = int((res + dp[i][j]) % mod)
        return res

# update: use another dp to find the actual maximum profit

class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # max_profit = sum(profit)

        dp = [0] * (n+1)
        dp[0] = 1
        for w, v in zip(group, profit):
            for i in range(n, w-1, -1):
                dp[i] = max(dp[i], dp[i-w]+v)
        max_profit = dp[n]

        dp = [[0] * (max_profit+1) for _ in range(n+1)]
        dp[0][0] = 1
        mod = 1e9+7
        for w, v in zip(group, profit):
            for i in range(n, w-1, -1):
                for j in range(max_profit, v-1, -1):
                    dp[i][j] = (dp[i][j] + dp[i-w][j-v]) % mod
        
        res = 0
        for i in range(n+1):
            for j in range(minProfit, max_profit+1):
                res = int((res + dp[i][j]) % mod)
        return res
                