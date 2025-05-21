# mine:
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = [True]*n
        row = [True]*n
        dig = [True]*2*n
        anti_dig = [True]*2*n
        q = []
        self.res = 0
        
        def dfs(row_index,queens):
            if row_index == n:
                self.res += 1
                return 
            else:
                for col_index in range(n):
                    if row[row_index] and col[col_index] and dig[row_index+col_index] and anti_dig[n-col_index+row_index]:
                        row[row_index] = col[col_index] = dig[row_index+col_index] = anti_dig[n-col_index+row_index] = False
                        tmp = queens.copy()
                        tmp.append([row_index,col_index])
                        dfs(row_index+1,tmp)
                        row[row_index] = col[col_index] = dig[row_index+col_index] = anti_dig[n-col_index+row_index] = True
        dfs(0,q)
        return self.res
