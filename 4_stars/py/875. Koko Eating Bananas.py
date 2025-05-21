# BS. implement from the simpler version and then, simplify it. Don't directly try to solve the problem in optimal way.

# reference: https://leetcode.com/problems/koko-eating-bananas/solutions/4160639/python-3-bs-pattern-similar-problems/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def isSufficientSpeed(cnt):
            return sum(ceil(i/cnt) for i in piles) <= h

        while l < r:
            m = (l + r)//2
            if isSufficientSpeed(m):
                r = m
            else:
                l = m + 1

        return l
