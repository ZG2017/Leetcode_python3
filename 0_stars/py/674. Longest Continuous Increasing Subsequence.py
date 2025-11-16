class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur_res = 0
        max_res = 0
        cur_max = -float('inf')
        for i in range(len(nums)):
            if nums[i] > cur_max:
                cur_res += 1
                cur_max = nums[i]
            else:
                max_res = max(max_res, cur_res)
                cur_max = nums[i]
                cur_res = 1
        max_res = max(max_res, cur_res)
        return max_res
             