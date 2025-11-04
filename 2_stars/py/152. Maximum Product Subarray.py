# pointer 
# 2 pass: first pass from left to right, second pass from right to left.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 1
        n = len(nums)
        cur_max = -float('inf')
        for i in range(n):
            if nums[i] != 0:
                c *= nums[i]
                cur_max = max(cur_max, c)
            else:
                c = 1
                cur_max = max(cur_max, 0)
        
        c = 1
        for i in range(n-1, -1, -1):
            if nums[i] != 0:
                c *= nums[i]
                cur_max = max(cur_max, c)
            else:
                c = 1
                cur_max = max(cur_max, 0)
        return cur_max

