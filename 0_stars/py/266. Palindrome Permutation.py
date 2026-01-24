class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd = False
        for v in counter.values():
            if v%2==1:
                if not odd:
                    odd = True
                else:
                    return False
        return True
