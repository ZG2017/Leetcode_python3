# bitmask + set of tuples to avoid duplicates
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        seen = set()
        
        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            seen.add(tuple(subset))

        return [list(t) for t in seen]
