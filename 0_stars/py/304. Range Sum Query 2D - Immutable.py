# mine:
class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.dp1 = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix))]
        self.dp2 = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix))]
        self.sums = [0 for _ in range(len(matrix))]
        for j in range(len(matrix)):
            self.dp1[j][1] = matrix[j][0]
            self.dp2[j][len(matrix[j])-2] = matrix[j][-1]
            for i in range(2,len(matrix[j])):
                self.dp1[j][i] = self.dp1[j][i-1] + matrix[j][i-1]
            for i in reversed(range(len(matrix[j])-2)):
                self.dp2[j][i] = self.dp2[j][i+1] + matrix[j][i+1]
            self.sums[j] = self.dp1[j][-2] + self.dp2[j][len(matrix[j])-2]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1,row2+1):
            res += self.sums[i] - self.dp1[i][col1] - self.dp2[i][col2]
        return res


# # Your NumMatrix object will be instantiated and called as such:
# # obj = NumMatrix(matrix)
# # param_1 = obj.sumRegion(row1,col1,row2,col2)


# updated: (clever: dp[r][c] represents sum from [0,0] to [r,c])
class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if self.matrix and self.matrix[0]:
            self.row = len(self.matrix)
            self.col = len(self.matrix[0])
            self.sumMatrix = [[0] * self.col for _ in range(self.row)]
            for r in range(self.row):
                for c in range(self.col):
                    self.sumMatrix[r][c] = matrix[r][c] 
            for r in range(1, self.row):
                self.sumMatrix[r][0] += self.sumMatrix[r - 1][0]
            for c in range(1, self.col):
                self.sumMatrix[0][c] += self.sumMatrix[0][c - 1]
            for r in range(1, self.row):
                for c in range(1, self.col):
                    self.sumMatrix[r][c] += self.sumMatrix[r - 1][c] + self.sumMatrix[r][c - 1] - self.sumMatrix[r - 1][c - 1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = self.sumMatrix[row2][col2]
        rowMinus = self.sumMatrix[row1 - 1][col2] if 0 < row1 else 0
        colMinus = self.sumMatrix[row2][col1 - 1] if 0 < col1 else 0
        rowColPlus = self.sumMatrix[row1 - 1][col1 - 1] if 0 < row1 and 0 < col1 else 0
        return total - rowMinus - colMinus + rowColPlus



# # Your NumMatrix object will be instantiated and called as such:
# # obj = NumMatrix(matrix)
# # param_1 = obj.sumRegion(row1,col1,row2,col2)
