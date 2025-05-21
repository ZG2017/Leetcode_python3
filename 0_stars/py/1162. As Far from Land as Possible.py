# BFS: ETL

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        memo = dict()
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = deque([(i, j, 1)])
                    visited = set()
                    while stack:
                        cur = stack.popleft()
                        for d in ds:
                            if cur[0]+d[0] in range(n) and cur[1]+d[1] in range(n) and grid[cur[0]+d[0]][cur[1]+d[1]] == 0 and (cur[0]+d[0], cur[1]+d[1]) not in visited:
                                stack.append((cur[0]+d[0], cur[1]+d[1], cur[2]+1))
                                visited.add((cur[0]+d[0], cur[1]+d[1]))
                                if (cur[0]+d[0], cur[1]+d[1]) not in memo:
                                    memo[(cur[0]+d[0], cur[1]+d[1])] = cur[2]
                                memo[(cur[0]+d[0], cur[1]+d[1])] = min(memo[(cur[0]+d[0], cur[1]+d[1])], cur[2])
        
        res = -1
        for i in memo.values():
            if i > res:
                res = i
        return res



# updated:

# BFS: wrt the layer
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        stack = deque()
        visited = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    visited.add((i, j))
        
        res = 0
        while stack:
            for i in range(len(stack)):
                cur = stack.popleft()
                for d in ds:
                    if cur[0]+d[0] in range(n) and cur[1]+d[1] in range(n) and (cur[0]+d[0], cur[1]+d[1]) not in visited:
                        stack.append((cur[0]+d[0], cur[1]+d[1]))
                        visited.add((cur[0]+d[0], cur[1]+d[1]))
            res += 1
        
        return res-1 if res-1 != 0 else -1



