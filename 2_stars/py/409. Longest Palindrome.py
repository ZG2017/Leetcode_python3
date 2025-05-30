# hashmap:
for even number just add,
for odd number add the max one,
for the rest of odd numbers add counter-1

class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        holder = Counter(s)
        res = 0
        max_odd = 0
        for _, c in holder.items():
            if c % 2 == 0:
                res += c
            else:
                if c > max_odd:
                    if max_odd != 0:
                        res -= 1
                    max_odd = c
                    res += c
                else:
                    res += c-1
        return res
