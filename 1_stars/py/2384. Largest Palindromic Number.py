# hashmap + counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter
        digit_holder = Counter(num)
        even_holder = dict()
        remain_holder = set()
        for i in digit_holder:
            if digit_holder[i]%2 == 0:
                even_holder[i] = digit_holder[i]
            else:
                if digit_holder[i] == 1:
                    remain_holder.add(i)
                else:
                    even_holder[i] = digit_holder[i]-1
                    remain_holder.add(i)
        p1, p2 = '', ''
        for idx, (digit, c) in enumerate(sorted(even_holder.items(), reverse=True, key=lambda x:x[0])):
            if digit == '0' and idx == 0:
                continue
            p1 += digit*(c//2)
            p2 = digit*(c//2) + p2
        if remain_holder:
            p1 += max(remain_holder)
        if len(p1+p2) != 0:
            return p1+p2
        else:
            return '0' 