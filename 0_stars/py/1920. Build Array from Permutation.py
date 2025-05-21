class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        ans = [nums[nums[i]] for i in range(lens)]
        return ans
        
