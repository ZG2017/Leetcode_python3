class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        cur_start = 0
        cur_end = 0+m
        c = 0
        while cur_end<=len(arr)-1:
            cur_pattern = arr[cur_start:cur_end]
            for i in range(k):
                if arr[cur_start+m*i:cur_end+m*i] == cur_pattern:
                    c += 1
                else:
                    break
            if c == k:
                return True
            else:
                c = 0
            cur_start += 1
            cur_end += 1
        return False
