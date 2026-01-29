# 2 pointer solution
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r = 0, -1
        best = 0
        counts = defaultdict(int)
        chars = set()
        while l < len(s):
            if len(chars) <= 2:
                best = max(best, r - l + 1)
            
            if r < len(s) - 1 and len(chars) <= 2:
                r += 1
                counts[s[r]] += 1
                chars.add(s[r])
            else:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    chars.remove(s[l])
                l += 1
        
        return best