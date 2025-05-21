# mine: dp
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) <=2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return max(dp[-1],dp[-2])


# updated: dp simpler
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = 0
        prev2 = 0
        temp = 0
        for x in nums:
            temp = prev1
            prev1 = max((x + prev2), prev1)
            prev2 = temp
            
        return prev1




        
        
