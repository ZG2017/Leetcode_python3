# for loop through nums instead of lower to upper.
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        ans = []
        for num in nums:
            if num > lower:
                ans.append([lower, num - 1])
            lower = num + 1
        if lower <= upper:
            ans.append([lower, upper])
        return ans