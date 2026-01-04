# priority queue (heap)
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        import heapq
        # transfer encode to range
        range_lights = []
        for p, r in lights:
            range_lights.append((p-r, p+r))
        
        range_lights.sort(key=lambda x:x[0])
        
        # compute max
        q = []
        max_c = 0
        cur_c = 0
        ans = float('inf')
        for start, end in range_lights:
            if not q:
                heapq.heappush(q, end)
                cur_c += 1
            else:
                while q and q[0] < start:
                    heapq.heappop(q)
                    cur_c -= 1
                heapq.heappush(q, end)
                cur_c += 1

            if cur_c > max_c:
                max_c = cur_c
                ans = start
        return ans
                        
    