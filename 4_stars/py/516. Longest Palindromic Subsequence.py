# dp

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s)) for _ in range(len(s))]
        for h in range(len(s)):
            dp[h][0] = 1
        for g in range(1, len(s)):
            for h in range(len(s)-g):
                tmp_l_idx = s[h:h+g].find(s[h+g])
                if tmp_l_idx == -1:
                    cur_if_use = 0
                else:
                    tmp_l_idx += h
                    if h+g-tmp_l_idx-2 == 0:
                        tmp = 1
                    elif h+g-tmp_l_idx-2 < 0:
                        tmp = 0
                    else:
                        tmp = dp[tmp_l_idx + 1][h+g-tmp_l_idx-2]
                    cur_if_use = tmp + 2
                dp[h][g] = max(dp[h][g-1], cur_if_use)
        return dp[0][len(s)-1]


# update: two pointer recursive with functools.cache

# refer: https://leetcode.com/problems/longest-palindromic-subsequence/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days

# from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def search_palindromes(s):
            if not s:
                return 0
            longest_palindrome = 1
            for character in string.ascii_lowercase:
                index_forward, index_backward = s.find(character), s.rfind(character)
                if index_forward != index_backward:
                    longest_palindrome = max(longest_palindrome, search_palindromes(s[index_forward+1:index_backward]) + 2)
            return longest_palindrome
        return search_palindromes(s)

