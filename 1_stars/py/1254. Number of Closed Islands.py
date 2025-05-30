# backtracking
class Solution:
    def backtracking(self, i, j, visited):
        if i < 0 or i > self.h-1 or j < 0 or j > self.w-1:
            return False
        if (i, j) in self.overall_visited:
            return self.overall_visited[(i, j)]
        if self.grid[i][j] == 1:
            self.overall_visited[(i, j)] = True
            return True
        if (i, j) in visited:
            return True
        if 0 == i or i == self.h-1 or 0 == j or j == self.w-1:
            self.overall_visited[(i, j)] = False
            return False
        for delta_i, delta_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (i + delta_i, j + delta_j) in visited:
                continue
            if not self.backtracking(i + delta_i, j + delta_j, visited + [(i, j)]):
                self.overall_visited[(i, j)] = False
                return False
        self.overall_visited[(i, j)] = True
        return True


    def closedIsland(self, grid: List[List[int]]) -> int:
        self.w = len(grid[0])
        self.h = len(grid)
        self.grid = grid
        self.overall_visited = dict()

        c = 0
        for idx_i in range(self.h):
            for idx_j in range(self.w):
                if grid[idx_i][idx_j] == 0 and (idx_i, idx_j) not in self.overall_visited:
                    if self.backtracking(idx_i, idx_j, []):
                        c += 1
        return c 