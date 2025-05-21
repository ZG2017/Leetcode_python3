class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            len_a = len(a)
            len_b = len(b)
            if len_a > len_b:
                return len_a
            else:
                return len_b
