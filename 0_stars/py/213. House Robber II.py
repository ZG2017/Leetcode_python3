# mine:(double dp)
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 or len(nums) == 2:
            return max(nums)
        dp1 = [0 for _ in range(len(nums)-1)]
        dp2 = [0 for _ in range(len(nums)-1)]
        dp1[0] = nums[0]
        dp1[1] = max(nums[0],nums[1])
        dp2[0] = nums[1]
        dp2[1] = max(nums[1],nums[2])
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[i-2]+nums[i],dp1[i-1])
        for i in range(3,len(nums)):
            dp2[i-1] = max(dp2[i-3]+nums[i],dp2[i-2])
        return max(dp1[-1],dp2[-1])
