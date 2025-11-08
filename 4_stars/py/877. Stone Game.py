# mine: recursive dp with cache

class Solution:
    def stoneGame(self, piles) -> bool:
        from functools import lru_cache
        @lru_cache(None)
        def score(i, j, cur_round): # max stones of alice
            if i == j:
                return piles[i]
            if cur_round: # alice's round
                return max(piles[i] + score(i + 1, j, False), piles[j] + score(i, j - 1, False))
            else:
                # bob's round
                return min(piles[i] + score(i + 1, j, True), piles[j] + score(i, j - 1, True))
        final_score = score(0, len(piles) - 1, True)
        return final_score > sum(piles) - final_score