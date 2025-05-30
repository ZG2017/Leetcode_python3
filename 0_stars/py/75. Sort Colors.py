# mine:
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
	nums.sort()

# updated:
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        tmp = nums
        for index in range(len(nums)):
    
            if nums[index] == 2 and index < right:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            if nums[index] == 0 and index > left:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
