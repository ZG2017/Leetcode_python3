class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        if not nums:
            return 0
        stack = []
        nums.append(-float("inf"))
        res = 0
        for index in range(len(nums)):
            while stack and nums[index] < nums[stack[-1]]:
                res += index - stack.pop()
            stack.append(index)
        return res
                
            
