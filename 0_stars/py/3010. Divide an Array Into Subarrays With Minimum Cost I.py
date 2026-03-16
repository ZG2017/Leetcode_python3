# the answer equals to first num + smallest num in nums[1:] + second smallest num in nums[1:]
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        indexed_nums = [(i, idx) for idx, i in enumerate(nums)]
        first_num = indexed_nums[0]
        second_num = min(indexed_nums[1:])
        third_num = float('inf')
        for i, idx in indexed_nums[1:]:
            if i < third_num and \
                idx != first_num[1] and \
                idx != second_num[1]:
                third_num = i
        return first_num[0] + second_num[0] + third_num


