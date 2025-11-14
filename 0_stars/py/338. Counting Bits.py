# updated: dp (http://bookshadow.com/weblog/2016/03/18/leetcode-counting-bits/)
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        import math
        def helper(x):
            return int(2**int(math.log2(x)))
        dp = [0] + [0 for _ in range(num)]
        for i in range(1,num+1):
            dp[i] = dp[i-helper(i)]+1
        return dp


# updated: (bit computation + dp)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x >> 1] + (x & 1),
        return ans


# pure bit computation
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            tmp = 0
            while i > 0:
                tmp += 1
                i = i & (i-1)
            res.append(tmp)
        return res
        

