# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/solutions/7265510/maximum-total-damage-w-spell-casting-mos-n3hx/
# replace bin search with linear scan to speed up the process.

# dp: dp[i] = max damage using keys[0..i]
# trans: dp[i] = max(dp[i-1], dp[j] + gain[i])

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from collections import Counter

        # Count frequency of each value
        freq = Counter(power)

        # Sorted unique values
        keys = sorted(freq)
        n = len(keys)

        # Precompute total gain for each value
        # dp[i] = max damage using keys[0..i]
        dp = [0] * n
        dp[0] = keys[0] * freq[keys[0]]

        # Pointer to track last non-conflicting index
        j = 0

        for i in range(1, n):
            # Move j forward while it is still valid:
            # we want keys[j] <= keys[i] - 3
            while j < i and keys[j] <= keys[i] - 3:
                j += 1

            # Standard DP transition
            # take current key and make keys[i] * freq[keys[i]] + previous damage (dp[j-1]) as current damage value.
            # or not take current key and use previous damage as current damage value.
            dp[i] = max(dp[i - 1], keys[i] * freq[keys[i]] + (dp[j - 1] if j - 1 >= 0 else 0))

        return dp[-1]