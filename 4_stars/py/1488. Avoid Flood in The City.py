# https://leetcode.com/problems/avoid-flood-in-the-city/solutions/7254853/solution-by-la_castille-5bp5/

# idea
# 1. iterate the rains, used filled dict to save the lake that is filled.
# 2. when a lake is train on again, to avoid flood, we need to find a 0 day to dry it before this day.
# 3. we need to find the first 0 day after the previous fill day and before the current day.
# 4. use union find to find the first 0 day after the previous fill day and before the current day.
# 5. need to use compress path in union find to avoid TLE.


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        filled = dict()
        uf = UnionFind(rains)
        for i, lake in enumerate(rains):
            if lake != 0:
                if lake not in filled:
                    # add to fill
                    filled[lake] = i
                else:
                    # need to find a 0 day to dry
                    prev_fill_day_idx = filled[lake]
                    next_0_day_idx = uf.find(prev_fill_day_idx)
                    if next_0_day_idx < i:
                        ans[next_0_day_idx] = rains[prev_fill_day_idx]
                        uf.used_zero(next_0_day_idx)
                        filled.pop(lake)
                        filled[lake] = i
                    else:
                        return []
                ans[i] = -1
        return ans

class UnionFind():
    def __init__(self, rains):
        self.holder = dict()
        self.build(rains)
    
    def build(self, rains):
        curr_rains = rains + [-1] # fake boundary
        cur_0_idx = len(curr_rains)-1
        self.holder[cur_0_idx] = cur_0_idx
        for i in range(len(curr_rains)-2, -1, -1):
            if curr_rains[i] != 0:
                self.holder[i] = cur_0_idx
            else:
                cur_0_idx = i
                self.holder[i] = cur_0_idx
    
    def find(self, x):
        if self.holder[x] != x:
            self.holder[x] = self.find(self.holder[x])
        return self.holder[x]
    
    def used_zero(self, x):
        # assert rains[x] == 0
        self.holder[x] = x + 1
