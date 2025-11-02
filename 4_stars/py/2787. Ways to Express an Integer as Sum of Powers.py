# 0-1 knapsack problem
# dp[i] means the number of ways to express i as sum of powers
# for each powers, we can either include it or not include it.
# dp[i] = dp[i-candidate] + dp[i]

class Solution(object):
    def get_list(self, n, x):
        if n == 0:
            return []
        max_i = 0
        for i in range(1, n+1):
            if i**x == n:
                max_i = i
                break
            elif i**x < n:
                continue
            else:
                max_i = i-1
                break
        res = []
        for i in range(1, max_i+1):
            res.append(i**x)
        return res

    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1
        mod = 1e9+7
        candidate_list = self.get_list(n, x)
        for candidate in candidate_list:
            for i in range(n, candidate-1, -1):
                if candidate <= i:
                    dp[i] = int((dp[i] + dp[i-candidate]) % mod)
        return dp[n]

        

        


        
