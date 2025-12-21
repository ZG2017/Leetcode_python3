# for each cell, check next 3 cells to see if they are the same, both horizontally and vertically.
# https://leetcode.com/problems/candy-crush/solutions/723531/python-straightforward-solution-by-darsh-2vds/
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #start the while loop
        while True:
            # check for the candies to be crushed
            crush = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j>1 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                        crush |= {(i,j), (i,j-1), (i,j-2)}
                    if i>1 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                        crush |= {(i,j), (i-1,j), (i-2,j)}
                        
            # crush the candies.
            if not crush: break
            for i, j in crush:
                board[i][j] = 0
                    
            # drop the candies
            for col in range(len(board[0])):
                idx = len(board)-1
                for row in range(len(board)-1, -1, -1):
                    if board[row][col]>0:
                        board[idx][col] = board[row][col]
                        idx -= 1
                        
                for row in range(idx+1):
                    board[row][col] = 0
                    
        return board