# dp
# refer: https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/?envType=problem-list-v2&envId=dynamic-programming
# for each position i in a, it either use operation 1 or operation 2.
# dp[i] = dp[i - 1] + x: use x to change s1[i] to s2[i] (operation 1)
# dp[i] = dp[i - 2] + 2 * (a[i - 1] - a[i - 2]): use 2 times of the gaps to change switch a[i - 1] and a[i - 2] (a chain of operation 2).

class Solution(object):
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        cnt = 0
        for c in s1:
            if c == '1':
                cnt += 1
        for c in s2:
            if c == '1':
                cnt -= 1

        if cnt % 2 != 0:
            return -1

        a = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                a.append(i)

        n = len(a)
        dp = [10000000] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + x
            if i >= 2:
                dp[i] = min(dp[i], dp[i - 2] + 2 * (a[i - 1] - a[i - 2]))

        return dp[n] // 2