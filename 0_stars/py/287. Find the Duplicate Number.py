# mine:
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return int((sum(nums)-sum(set(nums)))/(len(nums)-len(set(nums))))
