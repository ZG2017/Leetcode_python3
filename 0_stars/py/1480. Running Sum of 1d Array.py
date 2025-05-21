class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c = 0
        ans = []
        for i in range(len(nums)):
            c += nums[i]
            ans.append(c)
        return ans
