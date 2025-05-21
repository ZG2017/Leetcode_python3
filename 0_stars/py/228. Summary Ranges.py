# mine:
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        template = "->"
        res = []
        tmp = []
        nums.append(float("inf"))
        for i in range(len(nums)-1):
            tmp.append(nums[i])
            if nums[i+1] == nums[i]+1:
                continue
            else:
                if len(tmp) == 1:
                    res.append(str(tmp[0]))
                else:
                    res.append(str(tmp[0])+template+str(tmp[-1]))
                tmp = []
        return res
