class Solution:
    def countSubstrings(self, s: str) -> int:
        new_s = ""
        for i in s:
            new_s += i + "#"
        s = "!#"+new_s+"?"
        res = 0
        holder = [1] * (len(s))
        right_limit = 0
        max_idx = 0
        for i in range(len(s)-1):
            if i <= right_limit:
                holder[i] = min(holder[2*max_idx-i], right_limit-i+1)
            while s[i+holder[i]] == s[i-holder[i]]:
                holder[i] += 1
            if i + holder[i] > right_limit:
                right_limit = i + holder[i] - 1
                max_idx = i
            res += holder[i]//2
        return res
