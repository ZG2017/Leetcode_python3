# dp[i] = number of people who learn the secret for the first time on day i
# dp[i] = sum(dp[i-forget+1:i-delay+1]) % mod   
# answer = sum(dp[n-forget+1:n+1]) % mod
# +1 because the first day is the day the secret is told.
# remember to deal with case i-forget+1 < 0

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(delay+1, n+1):
            dp[i] = sum(dp[max(0, i-forget+1):i-delay+1]) % mod
        
        ans = 0
        for i in range(n - forget + 1, n + 1):
            if i >= 1:
                ans = (ans + dp[i]) % mod

        return ans