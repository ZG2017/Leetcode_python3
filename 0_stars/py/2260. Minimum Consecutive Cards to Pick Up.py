class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards) == len(set(cards)):
            return -1
        
        holder = dict()
        min_gap = 10e5+1
        for idx, i in enumerate(cards):
            if i not in holder:
                holder[i] = -1
            if holder[i] != -1:
                cur_gap = idx-holder[i]+1
                if cur_gap < min_gap:
                    min_gap = cur_gap
            holder[i] = idx
        return min_gap
                    
        
        
