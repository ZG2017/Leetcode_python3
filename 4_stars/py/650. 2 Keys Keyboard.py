# approach_1: math
# devided by maximum possible factors everytime
# refer: https://leetcode.com/problems/2-keys-keyboard/solutions/5657975/98-33-easy-solution-with-ultimate-explanation/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days
# Runtime: 35ms; Beats: 77.31%
# Memory: 16.45MB; Beats: 86.63%

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        steps = 0
        factor = 2

        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1

        return steps


# approach_2(my original approach): recursive
# Runtime: 155ms; Beats: 29.77%
# Memory 16.58MB; Beats: 58.52%

class Solution:
    def helper(self, cur_n, quota, level):
        if cur_n == self.n:
            self.res = level
            return True
        elif cur_n > self.n:
            return False
        if quota == 0:
            if self.helper(cur_n, cur_n, level+1):
                return True
        elif quota == cur_n:
            if self.helper(cur_n + quota, quota, level+1):
                return True
        else:
            if self.helper(cur_n, cur_n, level+1):
                return True
            if self.helper(cur_n + quota, quota, level+1):
                return True
        return False

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n
        self.res = 0
        self.helper(1, 0, 0)
        return self.res



