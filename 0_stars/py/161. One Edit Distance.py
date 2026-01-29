# divide and conquer
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        i, j = 0, 0
        edits = 0
        while i < len(s) or j < len(t):
            if i < len(s) and j < len(t) and s[i] == t[j]:
                i += 1
                j += 1
            elif not edits and len(s) < len(t):
                j += 1
                edits += 1
            elif not edits and len(s) == len(t):
                i += 1
                j += 1
                edits += 1
            elif not edits and len(s) > len(t):
                i += 1
                edits += 1
            else:
                return False
        return edits == 1