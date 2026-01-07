# TLE solution: stack mat, and treat each non-zero element as bootom let of submatrix

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        prefix_mat = mat.copy()
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    prefix_mat[i][j] = 0
                    continue
                if i-1 >= 0 and prefix_mat[i-1][j] != 0:
                    prefix_mat[i][j] = prefix_mat[i-1][j] + 1
                else:
                    prefix_mat[i][j] = 1
        
        # print(prefix_mat)

        ans = dict()
        for i in range(m):
            for j in range(n):
                if prefix_mat[i][j] == 0:
                    continue
                for width_idx in range(j, n):
                    if prefix_mat[i][width_idx] == 0:
                        break
                    for cur_height in range(0, min(prefix_mat[i][j:width_idx+1])):
                        cur_width = width_idx - j + 1
                        # print(i, j, cur_width, cur_height+1)
                        # print('--------')
                        ans[(cur_width, cur_height+1)] = ans.get((cur_width, cur_height+1), 0) + 1
        # print(ans)
        return sum(ans.values())


# update solution: the inner iteration is used to count number of submatrices with current element as the bottom left corner, which can be removed by looking into the max height we can reach give current (i, j) and current width_idx.

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        prefix_mat = mat.copy()
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    prefix_mat[i][j] = 0
                    continue
                if i-1 >= 0 and prefix_mat[i-1][j] != 0:
                    prefix_mat[i][j] = prefix_mat[i-1][j] + 1
                else:
                    prefix_mat[i][j] = 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                cur_max_height = prefix_mat[i][j]
                if prefix_mat[i][j] == 0:
                    continue
                for width_idx in range(j, n):
                    if prefix_mat[i][width_idx] == 0:
                        break
                    cur_max_height = min(cur_max_height, prefix_mat[i][width_idx])
                    ans += cur_max_height
        return ans
