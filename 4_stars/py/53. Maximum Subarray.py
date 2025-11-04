# prefix sum
# cur_sum - cur_min = the maximum subarray sum ending at the current index

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        cur_min = 0
        cur_sum = 0
        res = -float('inf')
        for num in nums:
            cur_sum += num
            res = max(res, cur_sum - cur_min)
            cur_min = min(cur_min, cur_sum)
        return res