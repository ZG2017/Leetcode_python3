# mine:
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                break
            i += 1
        else:
            i = 0
        return nums[i]
