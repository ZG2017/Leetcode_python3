# mine:
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        tmp = []
        res = []
        def dfs(start,tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(start,n+1):
                dfs(i+1,tmp+[i])
        dfs(1,tmp)
        return res
