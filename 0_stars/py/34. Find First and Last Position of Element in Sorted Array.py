class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            tmp_1 = nums.index(target)
            nums = nums[::-1]
            tmp_2 = len(nums)-1-nums.index(target)
            return [tmp_1,tmp_2]
        else:
            return [-1,-1]
