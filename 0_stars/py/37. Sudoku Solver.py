# mine:(TLE)

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.row = [[] for _ in range(9)]
        self.col = [[] for _ in range(9)]
        self.box = [[] for _ in range(9)]
        self.blank = {}
        dit = set(["1","2","3","4","5","6","7","8","9"])
        
        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == '.':
                    self.blank[(i,j)] = []
                if num not in self.row[i] and num not in self.col[j] and num not in self.box[3*(i//3) + (j//3)]:
                    self.row[i].append(num)
                    self.col[j].append(num)
                    self.box[3*(i//3) + (j//3)].append(num)
                
        self.index_list = list(self.blank.keys())
        print(self.index_list[0])
        self.total_number_blank = len(self.blank)
                
        for i in self.blank.keys():
            tmp_row = set(self.row[i[0]])
            tmp_col = set(self.col[i[1]])
            tmp_box = set(self.box[3*(i[0]//3) + (i[1]//3)])
            self.blank[i] = list(dit - tmp_row|tmp_col|tmp_box)
        
        self.fill_the_blank(0,board)

    def fill_the_blank(self,which_blank,board):
        if which_blank >= self.total_number_blank:
            return True
        for i in range(len(self.blank[self.index_list[which_blank]])):
            tmp = self.blank[self.index_list[which_blank]][i] 
            if tmp not in self.row[self.index_list[which_blank][0]] and \
               tmp not in self.col[self.index_list[which_blank][1]] and \
               tmp not in self.box[3*(self.index_list[which_blank][0]//3) + (self.index_list[which_blank][1]//3)]:
                board[self.index_list[which_blank][0]][self.index_list[which_blank][1]] = tmp
                self.row[self.index_list[which_blank][0]].append(tmp)
                self.col[self.index_list[which_blank][1]].append(tmp)
                self.box[3*(self.index_list[which_blank][0]//3) + \
                (self.index_list[which_blank][1]//3)].append(tmp)
                if not self.fill_the_blank(which_blank+1,board):
                    self.row[self.index_list[which_blank][0]].pop()
                    self.col[self.index_list[which_blank][1]].pop()
                    self.box[3*(self.index_list[which_blank][0]//3) + (self.index_list[which_blank][1]//3)].pop()
                    board[self.index_list[which_blank][0]][self.index_list[which_blank][1]] = "."
                else:
                    return True
            else:
                continue
        return False



    """
    def fill_the_blank(self,which_blank,board):
        if which_blank >= self.total_number_blank:
            return True
        for i in range(len(self.blank[self.index_list[which_blank]])):
            
            if all(board[self.index_list[which_blank][0]][j] != tmp for j in range(9)) and\
               all(board[j][self.index_list[which_blank][1]] != tmp for j in range(9)) and\
               all(board[(self.index_list[which_blank][0]//3)*3+0][(self.index_list[which_blank][1]//3)*3+j] != tmp for j in range(3)) and\
               all(board[(self.index_list[which_blank][0]//3)*3+1][(self.index_list[which_blank][1]//3)*3+j] != tmp for j in range(3)) and\
               all(board[(self.index_list[which_blank][0]//3)*3+2][(self.index_list[which_blank][1]//3)*3+j] != tmp for j in range(3)):
                board[self.index_list[which_blank][0]][self.index_list[which_blank][1]] = tmp
                if not self.fill_the_blank(which_blank+1,board):
                    board[self.index_list[which_blank][0]][self.index_list[which_blank][1]] = "."
                else:
                    return True
            else:
                continue
        return False
    """


# upgraded:
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.recursive(0, 0, board)

    def recursive(self, i, j, board):
        if j >= 9:
            return self.recursive(i + 1, 0, board)
        if i == 9:
            return True

        if board[i][j] == ".":
            for num in range(1, 10):
                num_str = str(num)
                if all([board[i][col] != num_str for col in range(9)]) and \
                   all([board[row][j] != num_str for row in range(9)]) and \
                   all([board[i // 3 * 3 + count // 3][j // 3 * 3 + count % 3] != num_str for count in range(9)]):
                    board[i][j] = num_str
                    if not self.recursive(i, j + 1, board):
                        board[i][j] = "."
                    else:
                        return True
        else:
            return self.recursive(i, j + 1, board)
        return False



