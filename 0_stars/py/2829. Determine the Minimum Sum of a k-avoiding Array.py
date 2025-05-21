class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = []
        i = 1
        while 1:
            if k-i not in res or k-i <= 0:
                res.append(i)
            i += 1
            if len(res) == n:
                break
        return sum(res)

