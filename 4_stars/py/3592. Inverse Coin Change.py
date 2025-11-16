# check with knapsack

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        candidates = []
        # find first num
        for idx, i in enumerate(numWays):
            if i != 0:
                if i == 1:
                    candidates.append(idx+1)
                    break
                else:
                    return []
        cur_idx = idx+1

        if cur_idx == len(numWays):
            return candidates
        
        # knappack
        @cache
        def knappack(candidates, k):
            dp = [[0]*(k+1) for _ in range(len(candidates)+1)]
            for i in range(len(candidates)+1):
                dp[i][0] = 1
            
            for i in range(1, len(candidates)+1):
                for cur_k in range(1, k+1):
                    if candidates[i-1] <= cur_k:
                        dp[i][cur_k] = dp[i-1][cur_k] + dp[i][cur_k-candidates[i-1]]

                    if candidates[i-1] > cur_k:
                        dp[i][cur_k] = dp[i-1][cur_k]
            return dp[len(candidates)][k]
        
        def dfs(cur_idx, candidates, is_finished):
            if cur_idx == len(numWays):
                if is_finished:
                    return candidates, True
                else:
                    return [], False
            cur_amount, cur_ways = cur_idx + 1, numWays[cur_idx]
            real_ways = cur_ways - knappack(tuple(candidates), cur_amount)
            if real_ways == 0:
                ans, is_finished = dfs(cur_idx+1, candidates, True)
            elif real_ways == 1:
                ans, is_finished = dfs(cur_idx+1, candidates + [cur_idx+1], True)
            else:
                return [], False
            return ans, is_finished

        ans, is_finished = dfs(cur_idx, candidates, False)
        if is_finished:
            return ans
        else:
            return []

# https://leetcode.com/problems/inverse-coin-change/description/

def findCoins(self, num_ways: List[int]) -> List[int]:
    n = len(num_ways)
    num_ways = [1] + num_ways
    my_ways = [1] + [0] * n
    res = []

    for i in range(1, n + 1):
        # If `myWays[x] == numWays[x]`, move on.
        if my_ways[i] == num_ways[i]:
            continue

        # If `myWays[x] + 1 == numWays[x]` → add that value as a coin in our basket and update `myWays`, so `myWays[x...n]` accounts for ways with the new coin.
        if num_ways[i] - my_ways[i] == 1:
            res.append(i)
            for j in range(i, n + 1):
                my_ways[j] += my_ways[j - i]

        # If `myWays[x] + 1 < numWays[x]` → no solution. (*see below for why)
        else:
            return []
    return res