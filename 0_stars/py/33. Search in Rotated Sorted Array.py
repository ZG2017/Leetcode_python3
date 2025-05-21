class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pointer_1 = 0
        pointer_2 = len(nums)-1
        
        if len(nums) == 0:
            return -1
        
        while pointer_1 < pointer_2-1:
            if nums[pointer_1] == target:
                return pointer_1
            elif nums[pointer_2] == target:
                return pointer_2
            elif nums[pointer_1] < target and nums[pointer_2] < target:
                if nums[pointer_1] > nums[pointer_2]:
                    pointer_2 = int((pointer_2+pointer_1)/2)
                else:
                    pointer_1 = pointer_2
                    pointer_2 = len(nums)-1
            elif nums[pointer_1] > target and nums[pointer_2] > target:
                if nums[pointer_1] > nums[pointer_2]:
                    pointer_1 = int((pointer_2+pointer_1)/2)
                else:
                    pointer_2 = pointer_1
                    pointer_1 = 0
            elif nums[pointer_1] > target and nums[pointer_2] < target:
                pointer_1 = pointer_2
                pointer_2 = len(nums)-1
            elif nums[pointer_1] < target and nums[pointer_2] > target:
                pointer_1 = int((pointer_2+pointer_1)/2)
                
        if nums[pointer_1] == target:
            return pointer_1
        elif nums[pointer_2] == target:
            return pointer_2
        else:
            return -1
