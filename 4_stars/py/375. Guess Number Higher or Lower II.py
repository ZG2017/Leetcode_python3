# mine:
class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for gap in range(1, n):
            for lo in range(1, n+1-gap):
                hi = lo + gap
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi]) for x in range(lo, hi))
        return dp[1][n]

# update functional dp (bottom up)

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def score(i, j):
            if j-i == 1:
                return i+1
            elif j == i:
                return 0
            holder = []
            for k in range(i+1, j): 
                lower_case = score(i, k-1)
                higher_case = score(k+1, j)
                holder.append(k+1 + max(lower_case, higher_case))
            return min(holder)
        return score(0, n-1)