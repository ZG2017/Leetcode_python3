# recursive with cache

class Solution:
    @cache
    def helper(self, cur_idx, m):
        if cur_idx >= self.l:
            return 0
        cur_max = 0
        if cur_idx+2*m >= self.l:
            return self.pre_sum[-1] - self.pre_sum[cur_idx]
        for i in range(cur_idx+1, min(cur_idx+m*2, self.l)+1):
            cur_res = self.pre_sum[i] - self.pre_sum[cur_idx]
            future_res = self.pre_sum[-1] - self.pre_sum[i] - self.helper(i, max((i-cur_idx), m))
            if cur_res + future_res > cur_max:
                cur_max = cur_res + future_res
        return cur_max

    def stoneGameII(self, piles: List[int]) -> int:
        if not piles:
            return 0
        cur_sum = 0
        self.pre_sum = [cur_sum]
        for i in piles:
            cur_sum += i
            self.pre_sum.append(cur_sum)
        self.l = len(piles)
        return self.helper(0, 1)


# update: DP:
# refer: https://leetcode.com/problems/stone-game-ii/solutions/5662713/98-55-easy-solution-with-explanation/

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        dp = [[0] * (n + 1) for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])

        return dp[0][1]


# update dp with cache
# at each round, the goal is to maximize the score of the current player
# the maximize score equals to the stones we can get from the current round plus what is remaining for us after next round
# since the total number of stones is fixed, what is remaining for us after next round equals to total number of stones minus the maximize the score the other player can get at next round
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        prefix_sum = [0]
        tmp = 0
        for i in piles:
            tmp += i
            prefix_sum.append(tmp)

        @cache
        def max_score(cur_idx, m):
            if cur_idx + 2*m >= len(piles):
                return prefix_sum[-1] - prefix_sum[cur_idx]
            
            holder = []
            for i in range(1, 2*m+1):
                cur_pre_sum = prefix_sum[i+cur_idx] - prefix_sum[cur_idx]
                next_M = max(m, i)
                next_max_score = max_score(i+cur_idx, next_M)
                remain_total = prefix_sum[-1] - prefix_sum[i+cur_idx]
                holder.append(cur_pre_sum + remain_total - next_max_score)
            return max(holder)

        return max_score(0, 1)


