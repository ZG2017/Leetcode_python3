class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        parts = []
        bins = bin(n)[2:]
        for i, c in enumerate(reversed(bins)):
            if c == '1':
                parts.append(2**i)
        parts = list(reversed(parts))
        k = len(parts)
        prefix = [[0] * k for _ in range(k)]
        for i in range(k):
            prefix[i][i] = parts[k - 1 - i]
            for j in range(i + 1, k):
                prefix[i][j] = (prefix[i][j - 1] * parts[k - 1 - j]) % mod
        res = []
        for l, r in queries:
            res.append(prefix[l][r])
        return res