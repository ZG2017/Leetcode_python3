# mine:
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        total = int(0.5*len(nums)*(len(nums)+1))
        return total-sum(nums)
