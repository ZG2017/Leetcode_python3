class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)-1):
            cur_start, cur_end = points[i], points[i+1]
            # min_ = min(abs(cur_start[0]-cur_end[0]), abs(cur_start[1]-cur_end[1]))
            max_ = max(abs(cur_start[0]-cur_end[0]), abs(cur_start[1]-cur_end[1]))
            res += max_
        return res

