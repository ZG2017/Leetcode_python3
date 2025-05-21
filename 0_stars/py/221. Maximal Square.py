class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        left_holder = [0]*n
        right_holder = [n-1]*n
        height_holder = [0]*n

        res = 0

        for i in range(m):
            cur_left = 0
            for j in range(n):
                if matrix[i][j] == "0":
                    height_holder[j] = 0
                    left_holder[j] = 0
                    cur_left = j + 1
                else:
                    height_holder[j] += 1
                    left_holder[j] = max(left_holder[j], cur_left)
            
            cur_right = n-1
            for j in reversed(range(n)):
                if matrix[i][j] == "0":
                    right_holder[j] = n-1
                    cur_right = j-1
                else:
                    right_holder[j] = min(right_holder[j], cur_right)
            
            for j in range(n):
                tmp = min(height_holder[j], (right_holder[j]+1-left_holder[j]))
                if tmp*tmp > res:
                    res = tmp*tmp
        return res
