# 2 rounds of reverse
# first reverse each word
# then reverse the whole string

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def rev(left: int, rght: int)-> None:
            s[left: rght] = s[left: rght][::-1]


        prevSpace = 0
        for curr, ch in enumerate(s):
            if ch == ' ':
                rev(prevSpace, curr)
                prevSpace = curr + 1
                
        rev(prevSpace, len(s))
        s.reverse()
        