# mine:
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        tmp_max = -float("inf")
        for i in range(1,len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)


# updated:

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #canada algorithem / Kadane's algorithm
        
        currentnum = nums[0]
        maxnum = nums[0]

        
        for i in nums[1:]:
            currentnum = max(i, i + currentnum)
            if currentnum > maxnum:
                maxnum = currentnum
        return maxnum
                


