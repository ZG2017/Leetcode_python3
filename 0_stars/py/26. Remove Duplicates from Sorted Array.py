# my:
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)

# updated:
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)
