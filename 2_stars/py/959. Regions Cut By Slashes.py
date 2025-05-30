# dfs

# refer: https://leetcode.com/problems/regions-cut-by-slashes/solutions/5617528/dfs-solution-python3/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        adj = [[1]*n*3 for _ in range(n*3)]
        for i in range(n):
            for j in range(n):
                r = i*3
                c = j*3
                if grid[i][j]=="/":
                    adj[r+2][c] = 0
                    adj[r+1][c+1] = 0
                    adj[r][c+2] = 0
                elif grid[i][j]=="\\":
                    adj[r][c] = 0
                    adj[r+1][c+1] = 0
                    adj[r+2][c+2] = 0

        count = 0
        for i in range(n*3):
            for j in range(n*3):
                if adj[i][j] == 1:
                    self.dfs(adj, i, j)
                    count+=1


        return count


    def dfs(self, adj: List[str], i: int, j:int) -> int:
        size = len(adj)
        adj[i][j] = 0
        dir = [[-1,0],[0,-1],[0,1],[1,0]]
        for dx, dy in dir:
            x, y = i + dx, j + dy

            if(x<0 or x>=size or y<0 or y>=size or adj[x][y]==0):
                continue

            self.dfs(adj, x, y)



# updated: Graph Theory --> Union-Find algorithm

# refer: https://leetcode.com/problems/regions-cut-by-slashes/solutions/5615615/python-graph-theory-union-find-algorithm-disjoint-set/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = {}

        # Initialize the union-find parent for each triangle
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Each cell is represented by 4 triangles: 0 (top-left), 1 (top-right), 2 (bottom-right), 3 (bottom-left)
        def get_index(i, j, k):
            return (i * n + j) * 4 + k

        # Initialize all triangles
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    parent[get_index(i, j, k)] = get_index(i, j, k)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    union(get_index(i, j, 0), get_index(i, j, 3))
                    union(get_index(i, j, 1), get_index(i, j, 2))
                elif grid[i][j] == '\\':
                    union(get_index(i, j, 0), get_index(i, j, 1))
                    union(get_index(i, j, 2), get_index(i, j, 3))
                else:
                    union(get_index(i, j, 0), get_index(i, j, 1))
                    union(get_index(i, j, 1), get_index(i, j, 2))
                    union(get_index(i, j, 2), get_index(i, j, 3))

                # Union with right and bottom cells if possible
                if j + 1 < n:
                    union(get_index(i, j, 1), get_index(i, j + 1, 3))
                if i + 1 < n:
                    union(get_index(i, j, 2), get_index(i + 1, j, 0))

        # Count the number of distinct roots
        return sum(find(x) == x for x in parent)

