# memorialized dp
# dp[i][j] represent the answer probability started with i ml water in A and j ml water in B.
# probability of a dp[i][j] = 0.25 * (dp[i-4][j], dp[i-3][j-1], dp[i-2][j-2], dp[i-1][j-3])


# top-down memorized dp: TLE 
# class Solution:
#     def soupServings(self, n: int) -> float:
#         units = math.ceil(n / 25)

#         @cache
#         def calc_prob(soupA, soupB):
#             if soupA <= 0 and soupB <= 0:
#                 return 0.5
#             if soupA <= 0:
#                 return 1.0
#             if soupB <= 0:
#                 return 0.0
#             return 0.25 * (
#                 calc_prob(soupA - 4, soupB) +
#                 calc_prob(soupA - 3, soupB - 1) +
#                 calc_prob(soupA - 2, soupB - 2) +
#                 calc_prob(soupA - 1, soupB - 3)
#             )

#         return calc_prob(units, units)


# observed that when N > 5000, dp[n][n] - 1 < 1e-5, so add a constraint
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1
        units = math.ceil(n / 25)

        @cache
        def calc_prob(soupA, soupB):
            if soupA <= 0 and soupB <= 0:
                return 0.5
            if soupA <= 0:
                return 1.0
            if soupB <= 0:
                return 0.0
            return 0.25 * (
                calc_prob(soupA - 4, soupB) +
                calc_prob(soupA - 3, soupB - 1) +
                calc_prob(soupA - 2, soupB - 2) +
                calc_prob(soupA - 1, soupB - 3)
            )

        return calc_prob(units, units)