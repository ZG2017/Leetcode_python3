class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def gen(w):
            for i in w:
                yield i
            while True:
                yield ''
        res = ''
        g1 = gen(word1)
        g2 = gen(word2)
        for i in range(max(len(word1), len(word2))):
            res += g1.__next__()
            res += g2.__next__()
        return res
