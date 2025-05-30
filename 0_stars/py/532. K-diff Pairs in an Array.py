class Solution:
    def findPairs(self, nums, k):
        if len(nums)<=1:
            return 0
        elif len(nums) == 2:
            if max(nums)-min(nums) == k:
                return 1
            else:
                return 0
        nums = sorted(nums)
        p1 = 0
        p2 = 1
        res = set([])
        while p1 < len(nums) or p2 < len(nums):
            if p2 == len(nums):
                p2 -= 1
                p1 += 1
            if p1 == len(nums):
                break
            if nums[p2] - nums[p1] == k:
                res.add((nums[p1], nums[p2]))
                p2 += 1
            elif nums[p2] - nums[p1] < k:
                p2 += 1
            else:
                p1 += 1
                if p1 == p2:
                    p2 += 1
        return len(res)
