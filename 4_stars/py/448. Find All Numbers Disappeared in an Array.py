# treat each integer in nums as na index, and set all index(integer) that appear in nums to negative.
# Then, the remaining positive index are the integers that don't show up in nums.

# space O(0)
# time O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i < 0:
                if nums[-i-1] > 0:
                    nums[-i-1] = -nums[-i-1]
            else:
                if nums[i-1] > 0:
                    nums[i-1] = -nums[i-1]
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

