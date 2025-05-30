# mine:

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums)-1
        start = 0
        while end >= start:
            tmp = int((end+start)/2)
            if nums[tmp] == target:
                return tmp
            elif nums[tmp] > target:
                end = tmp-1
            elif nums[tmp] < target:
                start = tmp+1
        return start


# updated:

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tmp = [i for i in nums if i<target]
        return len(tmp)
