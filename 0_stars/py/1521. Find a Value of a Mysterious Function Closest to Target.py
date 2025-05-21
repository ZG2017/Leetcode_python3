# time limit exceeded:
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res = inf
        for i in range(len(arr)):
            res = min(abs(arr[i]-target), res)
        for i in range(len(arr)):
            cur = arr[i]
            pre_cur = arr[i]
            for j in range(i+1, len(arr)):
                pre_cur = cur
                cur = cur&arr[j]
                if pre_cur >= target >= cur:
                    res = min(abs(pre_cur-target), abs(cur-target), res)
                    break
            res = min(abs(cur-target), res)
        return res


# 1. try to save the computed results in a set
# 2. sequencial '&' makes number smaller and smaller 

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res = inf
        seen = set([0xffffffff])
        for i in arr:
            cur_seen = set([0xffffffff])
            for j in seen:
                cur = i&j
                res = min(abs(cur-target), res)
                if cur > target: 
                    cur_seen.add(cur)
            seen = cur_seen
        return res
                

