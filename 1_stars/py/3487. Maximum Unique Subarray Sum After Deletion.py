class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n < 0 for n in nums):
            return max(nums)
        else:
            return sum(n for n in set(nums) if n > 0)
