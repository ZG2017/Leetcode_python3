# mine:
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        holder_high = None
        holder_low = None
        tmp = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    holder_high = i
                    holder_low = j
                    
        if holder_high == None and holder_low == None:
            nums.sort()
        else:
            tmp = nums[holder_high]
            nums[holder_high] = nums[holder_low]
            nums[holder_low] = tmp

	    #nums[holder_high+1:] = sorted(nums[holder_high+1:])
            for _ in range(len(nums)-1-holder_high-1):
                for j in range(holder_high+1,len(nums)-1):
                    if nums[j]>nums[j+1]:
                        tmp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = tmp






