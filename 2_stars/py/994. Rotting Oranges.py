# queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        if len(grid) == 0:
            return 0
        m,n = len(grid), len(grid[0])
        r_q = deque()
        f_c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    r_q.append((i,j))
                elif grid[i][j] == 1:
                    f_c += 1
        if f_c == 0:
            return 0
        res = 0
        while r_q:

            cur_len = len(r_q)
            for i in range(len(r_q)):
                x, y = r_q.popleft()
                for n_x, n_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= n_x < m and 0 <= n_y < n and grid[n_x][n_y] == 1:
                        grid[n_x][n_y] = 2
                        f_c -= 1
                        r_q.append((n_x, n_y))
            res += 1
            if f_c == 0:
                break

        if f_c != 0:
            return -1
        else:
            return res

