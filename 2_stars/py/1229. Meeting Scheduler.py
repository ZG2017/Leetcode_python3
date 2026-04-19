# compare one by one using 2 indexes

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        
        p1, p2 = 0, 0
        while p1 < len(slots1) and p2 < len(slots2):
            s1, e1 = slots1[p1]
            s2, e2 = slots2[p2]
            if e1 < s2:
                p1 += 1
                continue
            if e2 < s1:
                p2 += 1
                continue
            
            if min(e1, e2) - max(s1, s2) >= duration:
                return [max(s1, s2), max(s1, s2) + duration]
            
            if e1 < e2:
                p1 += 1
            elif e2 < e1:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return []
            
            


