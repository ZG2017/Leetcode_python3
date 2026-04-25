# brute force. scan throught each value, and grow from there until the square is not valid.
# O(m*n*min(m,n))

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 1

        def isValid(i, j, k):
            s = None
            for x in range(i, i + k):
                row = sum(grid[x][j:j + k])
                if s is None: s = row
                elif s != row: return False

            for y in range(j, j + k):
                if sum(grid[x][y] for x in range(i, i + k)) != s:
                    return False

            if sum(grid[i + d][j + d] for d in range(k)) != s:
                return False

            if sum(grid[i + d][j + k - 1 - d] for d in range(k)) != s:
                return False

            return True

        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if isValid(i, j, k):
                        res = k
        return res


# optimized with prefix sum
# use prefix sum to calculate the sum of the square in O(1) time

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        r, c= len(grid), len(grid[0])

        rowSum=[list(accumulate(row, initial=0)) for row in grid]
        # use tranpose matrix trick
        colSum=[list(accumulate(col, initial=0)) for col in zip(*grid)]

        diag, antidiag=([[0]*(c+1) for _ in range(r+1)] for _ in range(2))

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                diag[i+1][j+1]=diag[i][j]+x
                antidiag[i+1][j]=antidiag[i][j+1]+x

        def isMagic(k):
            for i in range(r-k+1):
                for j in range(c-k+1):
                    Sum=diag[i+k][j+k]-diag[i][j]
                    antiD=antidiag[i+k][j]-antidiag[i][j+k]
                    match=(Sum==antiD)

                    for m in range(k):
                        if not match: break
                        match=(
                            Sum==rowSum[i+m][j+k]-rowSum[i+m][j]
                            and Sum==colSum[j+m][i+k]-colSum[j+m][i]
                        )

                    if match:
                        return True
            return False

        for k in range(min(r, c), 1, -1):
            if isMagic(k): return k
        return 1

       