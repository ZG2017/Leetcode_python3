# mine:
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        max_gap = 0
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>max_gap:
                max_gap = nums[i]-nums[i-1]
        return max_gap
