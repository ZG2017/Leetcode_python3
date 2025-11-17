# dp


class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        dp = [[False] * (len(s)+1) for _ in range(len(s)+1)]
        for i in range(0, len(s)):
            dp[i][0] = True
        res = 0
        for len_ in range(1, len(s)+1):
            for i in range(0, len(s) + 1 - len_):
                if len_ == 1:
                    dp[i][len_] = dp[i][len_-1] & (s[i] == s[i+len_-1])
                else:
                    dp[i][len_] = dp[i+1][len_-2] & (s[i] == s[i+len_-1])
                if dp[i][len_]:
                    res += 1

        return res
