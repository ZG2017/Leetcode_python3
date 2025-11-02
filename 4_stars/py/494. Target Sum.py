# dp (0-1 knapsack problem)
# the real target (summation of one subset) is (target+sum(nums))/2
# we need to find the number of combinations to make up the real target, which is standard 0-1 knapsack problem.

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum_ = sum(nums)
        if (target+sum_)%2 != 0:
            return 0
        real_target = (target+sum_)//2
        
        if real_target < 0:
            return 0
        
        dp = [0] * (real_target+1)
        dp[0] = 1
        for num in nums:
            for i in range(real_target, num-1, -1):
                dp[i] = dp[i] + dp[i-num]
        return dp[real_target]