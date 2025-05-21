# binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) < 1:
        i, j = 0, len(nums)-1
        while i < j-1:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid
            else:
                j = mid
        if nums[j] != target and nums[i] != target:
            return -1
        elif nums[j] == target:
            return j
        else:
            return i 