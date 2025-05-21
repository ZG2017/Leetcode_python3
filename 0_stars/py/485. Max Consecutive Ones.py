class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        max_ = 0
        for i in nums:
            if i == 1:
                cur += 1
                if cur > max_:
                    max_ = cur
            else:
                cur = 0
        return max_
