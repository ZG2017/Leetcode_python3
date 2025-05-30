# pointer + greedy

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        res = 0
        tmp = sorted_nums[0]+1

        for num in sorted_nums[1:]:
            tmp = max(tmp, num)
            res += tmp - num
            tmp += 1
        return res

