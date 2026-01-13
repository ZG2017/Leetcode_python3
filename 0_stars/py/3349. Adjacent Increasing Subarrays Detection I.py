# 2 pointer solution
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        p1, p2 = 0, k
        k_counter = k - 1
        if k_counter == 0:
            return True
        while p2+1 < len(nums):
            if nums[p1] < nums[p1+1] and nums[p2] < nums[p2+1]:
                k_counter -= 1
            else:
                k_counter = k - 1
            if k_counter == 0:
                return True
            p1 += 1
            p2 += 1
        return False