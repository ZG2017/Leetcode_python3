class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        if not A:
            return 0
        dp = [0 for i in range(len(A))]
        total_sum = sum(A)
        first = 0
        for idx, val in enumerate(A):
            first += idx*val
        dp[0] = first
        p = len(A)-1
        for i in range(1, len(A)):
            dp[i] = dp[i-1] + total_sum - A[p]*(len(A)-1) - A[p]
            p -= 1
        return max(dp)
