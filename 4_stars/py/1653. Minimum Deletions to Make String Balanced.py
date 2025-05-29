# refer: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/solutions/5555960/easy-one-pass-o-1-space-solution-c-python-java/?envType=problem-list-v2&envId=dynamic-programming

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = count = 0
        for c in s:
            if c == 'b':
                count += 1
            elif count:
                res += 1
                count -= 1
        return res