class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_%2 == 1:
            return False

        target_n = sum(nums)//2
        dp = [False] * (target_n+1)
        dp[0] = True
        for i in nums:
            if i > target_n:
                return False
            for j in range(target_n, i-1, -1):
                dp[j] = dp[j] or dp[j-i]
        return dp[target_n]
