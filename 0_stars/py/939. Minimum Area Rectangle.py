# hashmap

class Solution:
    def is_rectangle(self, p1, p2):
        if p2[1] in self.x_holder[p1[0]] and p2[0] in self.y_holder[p1[1]]:
            return True
        else:
            return False

    def minAreaRect(self, points: List[List[int]]) -> int:
        self.y_holder = dict()
        self.x_holder = dict()

        for p in points:
            if p[0] not in self.x_holder:
                self.x_holder[p[0]] = [p[1]]
            else:
                self.x_holder[p[0]].append(p[1])
        
            if p[1] not in self.y_holder:
                self.y_holder[p[1]] = [p[0]]
            else:
                self.y_holder[p[1]].append(p[0])

        res = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1, p2 = points[i], points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                elif self.is_rectangle(p1, p2):
                    cur_res = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    if cur_res <= res:
                        res = cur_res
        if isinstance(res, float):
            return 0
        return res

            
