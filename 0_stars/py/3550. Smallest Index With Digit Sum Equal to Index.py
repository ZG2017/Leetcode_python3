class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx, i in enumerate(nums):
            if sum([int(j) for j in str(i)]) == idx:
                return idx
        return -1