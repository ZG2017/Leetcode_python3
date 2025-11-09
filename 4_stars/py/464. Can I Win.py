# top-down dp with cache
# check if we can directly win, or
# check if opponent can win in next round

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        m = maxChoosableInteger
        target = desiredTotal
        if m * (m + 1) // 2 < target:
            return False
        if target <= m:
            return True
        nums = list(range(m, 0, -1))

        @cache
        def win(used_mask: int, remain: int) -> bool:
            for x in nums:
                bit = 1 << (x - 1)
                if used_mask & bit:  
                    continue
                if x >= remain:
                    return True
                nxt = used_mask | bit
                if not win(nxt, remain - x):
                    return True       
            return False          
        return win(0, target)