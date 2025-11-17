class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        c = Counter(text)
        cur_min = float('inf')
        for letter in 'balloon':
            if letter in c:
                if letter not in 'lo':
                    cur_min = min(cur_min, c[letter])
                else:
                    cur_min = min(cur_min, c[letter]//2)
            else:
                return 0
        return cur_min
