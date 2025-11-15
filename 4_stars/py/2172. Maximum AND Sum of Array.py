# dp with bitmask
# dp[mask] means the maximum AND sum of the array with the current mask

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        m = 2 * numSlots  # total positions

        @cache
        def dp(mask: int) -> int:
            # how many numbers have been assigned so far?
            k = mask.bit_count()
            if k == n:
                return 0  # all numbers assigned

            num = nums[k]
            best = 0

            # try to place nums[k] into any free position
            for pos in range(m):
                if not (mask & (1 << pos)):  # this position is free
                    slot = pos // 2 + 1      # slot index is 1-based
                    cand = (num & slot) + dp(mask | (1 << pos))
                    if cand > best:
                        best = cand

            return best

        return dp(0)

