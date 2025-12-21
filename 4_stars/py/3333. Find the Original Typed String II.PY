# sliding window + DP
# run-length encoding to get groups e.g. "aaabbbcc" -> [3, 3, 2]
# total combinations = product of all groups count
# invalid combinations = sum of dp[j-1]..dp[j-g], where dp[j] is the number of valid combinations of length j
# answer = total combinations - invalid combinations (length of groups < k)
# answer = total combinations (length of groups >= k)

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        # 1) run-length encoding -> groups
        groups = []
        cnt = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                groups.append(cnt)
                cnt = 1
        groups.append(cnt)

        r = len(groups)

        # 2) total combinations (no length constraint)
        total = 1
        for g in groups:
            total = (total * g) % MOD

        # if minimum possible length already >= k
        if k <= r:
            return total

        # 3) count invalid (length < k) via DP
        dp = [0] * k
        dp[0] = 1  # empty before choosing any group

        for i, g in enumerate(groups):
            new = [0] * k
            window = 0
            # j starts from i because after i groups, min length is i
            for j in range(i, k):
                new[j] = window  # sum of dp[j-1]..dp[j-g]
                window = (window + dp[j]) % MOD
                if j >= g:
                    window = (window - dp[j - g] + MOD) % MOD
            dp = new

        invalid = sum(dp) % MOD
        return (total - invalid) % MOD