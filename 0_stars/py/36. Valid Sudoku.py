# mine:
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        tmp_row = [[] for _ in range(9)]
        tmp_column = [[] for _ in range(9)]
        tmp_box = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == "." and board[j][i] == ".":
                    continue
                elif board[i][j] == "." and board[j][i] != ".":
                    if board[j][i] not in tmp_column[i]:
                        tmp_column[i].append(board[j][i])
                    else:
                        return False
                elif board[i][j] != "." and board[j][i] == ".":
                    if board[i][j] not in tmp_row[i]:
                        tmp_row[i].append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in tmp_box[(i//3)*3+j//3]:
                        tmp_box[(i//3)*3+j//3].append(board[i][j])
                    else:
                        return False
                else:
                    if board[j][i] not in tmp_column[i]:
                        tmp_column[i].append(board[j][i])
                    else:
                        return False
                    if board[i][j] not in tmp_row[i]:
                        tmp_row[i].append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in tmp_box[(i//3)*3+j//3]:
                        tmp_box[(i//3)*3+j//3].append(board[i][j])
                    else:
                        return False
        return True

# upgrated:

class Solution:
    def isValidSudoku(self, board):
        row = [{} for _ in range(len(board))]
        col = [{} for _ in range(len(board))]
        box = [{} for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == '.':
                    continue
                if num not in row[i] and num not in col[j] and num not in box[3*(i//3) + (j//3)]:
                    row[i][num] = 1
                    col[j][num] = 1
                    box[3*(i//3) + (j//3)][num] = 1
                else:
                    return False
        return True
