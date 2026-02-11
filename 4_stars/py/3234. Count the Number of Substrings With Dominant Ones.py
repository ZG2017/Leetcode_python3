# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/solutions/7338477/count-the-number-of-substrings-with-domi-jqas/
# core idea: brute force is too slow, we can stop at cnt0 * cnt0 <= n, because if cnt0 * cnt0 > n, then the substring cannot be dominant.
# rest of the solution, check the official solution.


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res