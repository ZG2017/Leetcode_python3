class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set([])
        for i in range(len(nums[:-2])):
            if nums[i] == nums[i-1] and i >= 1:
                continue
            tmp = set([])
            for j in nums[i+1:]:
                if j not in tmp:
                    tmp.add(-j-nums[i])
                else:
                    res.add((nums[i],j,-nums[i]-j))
        res = list(res)
        return res
