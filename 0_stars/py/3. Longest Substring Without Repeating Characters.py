# mine:
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        holder = {}
        res = 0
        for index, char in enumerate(s):
            if char in holder and start <= holder[char]:
                start = holder[char] + 1
            holder[char] = index
            if index - start + 1 > res:
                res = index - start + 1
        return res

# updated:
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_start = 0
        longend = -1
        longstart = 0
        counter = {}
        for index, char in enumerate(s):
            if char in counter and current_start <= counter[char]:
                current_start = counter[char] + 1
            counter[char] = index
            if index-current_start>longend-longstart:
                longend = index
                longstart = current_start
        return longend - longstart + 1
