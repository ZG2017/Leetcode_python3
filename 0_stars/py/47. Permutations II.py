# mine:
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        
        def dfs(nums,tmp_permute):
            already = []
            if nums == []:
                res.append(tmp_permute)
            for i in range(len(nums)):
                if nums[i] in already:
                    continue
                else:
                    already.append(nums[i])
                tmp_nums = nums.copy()
                tmp_nums.pop(i)
                dfs(tmp_nums,tmp_permute + [nums[i]])
        
        dfs(nums,tmp)
        return res
