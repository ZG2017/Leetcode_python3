# from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(list(s))
        tmp = sorted(c.items(), key = lambda x: x[1], reverse = True)
        return "".join([i[0]*i[1] for i in tmp])
