# first, sort coins
# second, keep adding next unobtainable number to cur_max_obtainable.

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        sorted_coins = sorted(coins)
        cur_max_obtainable = 0
        add_c = 0
        p = 0
        for cur_coin in sorted_coins:
            while cur_max_obtainable < cur_coin-1:
                add_c += 1
                cur_max_obtainable += cur_max_obtainable+1
                if cur_max_obtainable >= target:
                    return add_c
            cur_max_obtainable += cur_coin
            if cur_max_obtainable >= target:
                return add_c

        while cur_max_obtainable < target:
            add_c += 1
            cur_max_obtainable += cur_max_obtainable+1
        return add_c


