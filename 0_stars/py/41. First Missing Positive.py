# mine:
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        
        return len(nums)+1
        
