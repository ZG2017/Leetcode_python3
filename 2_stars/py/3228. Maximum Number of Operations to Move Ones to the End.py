# to move continuous zeros subarray to the left, we need to move n times, where n is the number of ones on the left of the continuous zeros.

class Solution:
    def maxOperations(self, s: str) -> int:
        n_one = 0
        i = 0
        ans = 0
        while i < len(s):
            if s[i] == '1':
                n_one += 1
                i += 1
            else:
                i += 1
                cur_n_zero = 1
                while i < len(s) and s[i] == '0':
                    cur_n_zero += 1
                    i += 1
                ans += n_one
        return ans