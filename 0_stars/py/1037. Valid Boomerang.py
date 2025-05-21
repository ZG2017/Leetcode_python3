class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        holder = set([tuple(i) for i in points])
        if len(holder) < 3:
            return False
        if len(set([i[1] for i in points])) == 1 or len(set([i[0] for i in points])) == 1:
            return False
        if (points[0][1]-points[1][1])*(points[2][0]-points[1][0])== (points[0][0]-points[1][0])*(points[2][1]-points[1][1]):
            return False
        else:
            return True
