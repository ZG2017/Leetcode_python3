# mine:
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        index = [0,0]
        for _ in range(int((n**2+n)/2)):
            tmp = matrix[index[0]][index[1]]
            matrix[index[0]][index[1]] = matrix[n-index[1]-1][n-index[0]-1]
            matrix[n-index[1]-1][n-index[0]-1] = tmp
            index[1] += 1
            if index[1] >= n - index[0]:
                index[0] += 1
                index[1] = 0
        print(matrix)
        for i in range(n//2):
            tmp = matrix[i]
            matrix[i] = matrix[n-1-i]
            matrix[n-1-i] = tmp


# udpated:
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


