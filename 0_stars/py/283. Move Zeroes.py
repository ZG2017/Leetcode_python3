# mine:
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        counter = 0
        index = 0
        while index <= n-counter-1:
            if nums[index] == 0:
                nums.append(nums.pop(index))
                counter += 1
            else:
                index += 1
