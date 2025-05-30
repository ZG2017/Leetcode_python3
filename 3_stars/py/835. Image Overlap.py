# smart brute force

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        import numpy as np
        arr1, arr2 = np.array(img1, dtype=bool), np.array(img2, dtype=bool)
        n = len(img1)
        max_res = 0
        for i in range(0, 2*n):
            for j in range(0, 2*n):
                cur_arr1 = arr1[max(0, i-n):min(i, n), max(0, j-n):min(j, n)]
                r_i, r_j = n-i, n-j
                cur_arr2 = arr2[max(0, r_i):min(r_i+n, n), max(0, r_j):min(r_j+n, n)]
                cur_res = np.sum(cur_arr1 & cur_arr2)
                max_res = max(max_res, cur_res)
        return max_res

