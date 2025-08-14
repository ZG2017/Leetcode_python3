# n^2

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                else:
                    ans = max(ans, nums[j]-nums[i])
        return ans
    
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/solutions/6848844/easy-solution-eng-hing-explained-0-ms-o-n-greedy-sliding-window/
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far = nums[0]  
        ans = -1
        for i in range(1, len(nums)):  
            if nums[i] > min_so_far:
                ans = max(ans, nums[i] - min_so_far)
            else:
                min_so_far = nums[i]
        return ans  