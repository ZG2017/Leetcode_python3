# dp, add digit one by one from left to right

# refer: https://www.youtube.com/watch?v=dglwb30bUKI&t=1270s

# dp, TLE
# time O(n**2k)
# space(n*k)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = sum([dp[i-1][x] for x in range(max(j-i+1, 0), j+1)])
        return dp[n][k]

# updates dp, TLE
# time O(n**2k)
# space(k)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        prev = [0]*(k+1)
        prev[0] = 1

        for i in range(1, n+1):
            cur = [0]*(k+1)
            cur[0] = 1
            for j in range(1, k+1):
                cur[j] = sum([prev[x] for x in range(max(j-i+1, 0), j+1)])
            prev = cur
        return cur[k]


# updates dp + sliding window to replace sum()
# time O(nk)
# space(k)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        prev = [0]*(k+1)
        prev[0] = 1
        for i in range(1, n+1):
            cur = [0]*(k+1)
            cur[0] = 1
            sw = 1
            for j in range(1, k+1):
                if j-i+1 > 0:
                    sw += (prev[j] - prev[j-i])
                else:
                    sw += prev[j]
                cur[j] = sw
            prev = cur
        return cur[k] % (10**9 + 7)
