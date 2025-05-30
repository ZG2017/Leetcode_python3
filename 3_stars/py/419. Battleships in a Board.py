# DFS (bad solution)

class Solution:
    def check_index(self, x, y):
        if x >= 0 and x < self.len_col and y >= 0 and y < self.len_row:
            return True
        else:
            return False
    
    def get_direction(self, i, j):
        return (i-1, j), (i+1, j), (i,j-1), (i,j+1)
    
    def DFS(self, i, j):
        self.visited[i][j] = True
        for idx_i,idx_j in self.get_direction(i,j):
            if self.check_index(idx_i,idx_j) and self.matrix[idx_i][idx_j] == "X" and not self.visited[idx_i][idx_j]:
                self.DFS(idx_i, idx_j)
        return


    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        self.len_col = len(board)
        self.len_row = len(board[0])
        self.matrix = board
        res = 0
        self.visited = [[False for i in range(self.len_row)] for j in range(self.len_col)]
        for i in range(self.len_col):
            for j in range(self.len_row):
                if self.visited[i][j] or self.matrix[i][j] != "X":
                    continue
                else:
                    self.DFS(i,j)
                    res += 1
        return res
                    

# update: O(1) memory, O(mn) time

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if i - 1 >= 0 and j - 1 >= 0:
                        if board[i-1][j] == '.' and board[i][j-1] == '.':
                            res += 1
                    elif i - 1 >= 0 and j - 1 < 0:
                        if board[i-1][j] == '.':
                            res += 1
                    elif i - 1 < 0 and j - 1 >= 0:
                        if board[i][j-1] == '.':
                            res += 1
                    else:
                        res += 1
        return res

