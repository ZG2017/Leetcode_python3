# mod operation to get the index of the transformed array.
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * len(nums)
        for idx in range(n):
            if nums[idx] == 0:
                res[idx] = nums[idx]
            elif nums[idx] > 0:
                remain = nums[idx]%n + idx
                new_idx = remain if remain <= n-1 else remain - n
                res[idx] = nums[new_idx]
            else:
                remain = idx - abs(nums[idx])%n
                new_idx = remain if remain >= 0 else n + remain
                res[idx] = nums[new_idx]
        return res