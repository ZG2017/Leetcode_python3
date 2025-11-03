# dp

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 0:
            return 0
        if len(cost) <= 2:
            return min(cost)
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1, 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[len(cost)]