# dp with cache
# update dp with cache
# at each round, the goal is to maximize the score of the current player
# the maximize score equals to the stones we can get from the current round plus what is remaining for us after next round
# since the total number of stones is fixed, what is remaining for us after next round equals to total number of stones minus the maximize the score the other player can get at next round
# add 3 more times the prefix sum to tackle negative number of stones

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        tmp = 0
        prefix = [0]
        for i in stoneValue:
            tmp += i
            prefix.append(tmp)
        prefix.append(tmp)
        prefix.append(tmp)
        prefix.append(tmp)
        
        @cache
        def score(cur_idx):
            if cur_idx + 3 > len(prefix) - 1:
                return prefix[-1] - prefix[cur_idx]
            holder = []
            for i in range(1, 4):
                cur_stones = prefix[i + cur_idx] - prefix[cur_idx]
                future_stones = prefix[-1] - prefix[i + cur_idx] - score(i + cur_idx)
                holder.append(cur_stones + future_stones)
            return max(holder)

        max_stones = score(0)
        if 2 * max_stones > prefix[-1]:
            return 'Alice'
        elif 2 * max_stones < prefix[-1]:
            return 'Bob'
        else:
            return 'Tie'

# update dp with cache