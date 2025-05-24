# dp

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        if len(sequence) < len(word):
            return 0
        elif sequence == word:
            return 1
        dp = [0]*(len(sequence)+1)
        for i in range(len(word), len(sequence)+1):

            if sequence[i-len(word):i] == word:
                dp[i] = dp[i-len(word)] + 1
            else:
                dp[i] = 0
        return max(dp)


# update: even faster with binary search
# refer: https://leetcode.com/problems/maximum-repeating-substring/solutions/952687/python-binary-search-on-the-length-of-the-subsequence/?envType=problem-list-v2&envId=dynamic-programming

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        left = 1
        right = len(sequence) // len(word)
        while left <= right:
            mid = (left + right) // 2
            if word * mid in sequence:
                left = mid + 1
            else:
                right = mid - 1 
                
        return left - 1