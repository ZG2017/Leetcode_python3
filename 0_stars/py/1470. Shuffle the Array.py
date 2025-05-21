class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) == 0:
            return []
        a, b = nums[:n], nums[n:]
        res = []
        for i in zip(a,b):
            res.extend(i)
        return res
