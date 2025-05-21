from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        mapping = dict()
        c = 0
        for i in range(len(sorted_arr)):
            if i == 0 or (i != 0 and sorted_arr[i] != sorted_arr[i-1]):
                c += 1
            mapping[sorted_arr[i]] = c
        return [mapping[i] for i in arr] 