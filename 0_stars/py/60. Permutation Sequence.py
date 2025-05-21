# mine:
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dit = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}
        core = [str(i) for i in range(1,n+1)]
        res = []
        def find(n,k):
            if not n:
                return
            res.append(core.pop((k-1)//dit[n-1]))
            find(n-1,k%dit[n-1])
        find(n,k)
        return "".join(res)

# updated:
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dit = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}
        core = [str(i) for i in range(1,n+1)]
        res = []
        for _ in range(n):
            res.append(core.pop((k-1)//dit[n-1]))
            k -= ((k-1)//dit[n-1])*dit[n-1]
            n -= 1
        return "".join(res)
