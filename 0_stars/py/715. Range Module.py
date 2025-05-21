# binary search
# refer: https://leetcode.com/problems/range-module/solutions/5033868/writing-your-own-binary-search-python/

class RangeModule:

    def __init__(self):
        self.tracking = [] # non-overlapping ranges representing as (start, end)

    def _binary_search_q(self, val):
        l = 0
        h = len(self.tracking)*2-1 # tracking[m//2][m%2]
        while h >= l:
            m = (h + l) // 2
            if self.tracking[m//2][m%2] == val:
                return m//2, m//2
            elif self.tracking[m//2][m%2] > val:
                h = m - 1
            elif self.tracking[m//2][m%2] < val:
                l = m + 1
        return h//2, l//2
    def addRange(self, left: int, right: int) -> None: # O(n)
        l_l, l_h = self._binary_search_q(left)
        r_l, r_h = self._binary_search_q(right)
        if l_l != l_h:
            new_start = left
            remove_start = l_h
        else:
            new_start = self.tracking[l_l][0]
            remove_start = l_l
        if r_l != r_h:
            new_end = right
            remove_end = r_l
        else:
            new_end = self.tracking[r_h][1]
            remove_end = r_h
        self.tracking = self.tracking[:remove_start] + [(new_start, new_end)] + self.tracking[remove_end+1:]

    def queryRange(self, left: int, right: int) -> bool:
        l_l, l_h = self._binary_search_q(left)
        r_l, r_h = self._binary_search_q(right)
        if l_h == r_l == r_h == l_l:
            return True
        else:
            return False

    def removeRange(self, left: int, right: int) -> None: # O(n)
        l_l, l_h = self._binary_search_q(left)
        r_l, r_h = self._binary_search_q(right)
        inserting = []
        if l_l == r_l and l_h == r_h and l_l != l_h:
            return
        else:
            remove_start = self.tracking[l_h]
            remove_end = self.tracking[r_l]
            if left > remove_start[0]:
                inserting.append((remove_start[0], left))
            if remove_end[1] > right:
                inserting.append((right, remove_end[1]))

        self.tracking = self.tracking[:l_h] + inserting + self.tracking[r_l+1:] 