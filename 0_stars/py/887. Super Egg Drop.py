# 动态规划，（k, n）表示有K个鸡蛋，需要探测n层楼

# method1:思路方法正确， 但是超时了。
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        self.memo = dict()
        res = self.helper(K, N)
        return res
    def helper(self, k, n):
        if n <= 1:
            return 1
        elif k == 1 and n > 1:
            return n
        max_res = []
        for x in range(1, n):
            if (k-1, x-1) not in self.memo:
                self.memo[(k-1, x-1)] = self.helper(k-1, x-1)
            tmp1 = self.memo[(k-1, x-1)]
            if (k, n-x) not in self.memo:
                self.memo[(k, n-x)] = self.helper(k, n-x)
            tmp2 = self.memo[(k, n-x)]
            max_res.append(max(tmp1, tmp2))
        res = min(max_res)+1
        self.memo[(k, n)] = res
        return res

# method2：将for循环换为二分查找，（因为dp的单调性，详情见https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution-2/）
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)
