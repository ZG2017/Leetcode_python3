# mine:
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        # 3:1/0 4:0/1
        n = len(board)
        m = len(board[0])
        dit = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(n):
            for j in range(m):
                counter = 0
                for k in dit:
                    if (i+k[0]>=0 and i+k[0]<n and j+k[1]>=0 and j+k[1]<m) \
                    and (board[i+k[0]][j+k[1]] == 1 or board[i+k[0]][j+k[1]] == 3):
                        counter += 1
                if board[i][j] == 1 and (counter < 2 or counter > 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and counter == 3:
                    board[i][j] = 4
        for i in range(n):
            for j in range(m):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 4:
                    board[i][j] = 1
        
