# DFS+BFS

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        islands = [set(), set()]
        visited = set()
        from collections import deque
        q = deque()
        r, c = len(grid), len(grid[0])
        count = 0
        for i in range(r):
            if count == 2:
                break
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in visited:
                    q.append((i, j))
                    visited.add((i,j))
                    islands[count].add(((i,j), 0))
                    while q:
                        x, y = q.pop()
                        for dr, dc in direction:
                            if x+dr in range(r) and y+dc in range(c) and grid[x+dr][y+dc] == 1 and ((x+dr, y+dc), 0) not in islands[count]:
                                q.append((x+dr, y+dc))
                                visited.add((x+dr, y+dc))
                                islands[count].add(((x+dr, y+dc), 0))
                    count += 1
        
        q = deque(islands[0])
        visited = set()
        while q:
            (x, y), layer = q.popleft()
            for dr, dc in direction:
                if x+dr not in range(r) or y+dc not in range(c):
                    continue
                if ((x+dr, y+dc), 0) in islands[1]:
                    return layer
                if grid[x+dr][y+dc] == 0 and (x+dr, y+dc) not in visited:
                    q.append(((x+dr, y+dc), layer+1))
                    visited.add((x+dr, y+dc))
                res =+ 1
        return 0
         



            
                    
                    
        
        
                    
                    
                
                    
                        
        
