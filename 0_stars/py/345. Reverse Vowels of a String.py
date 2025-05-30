# mine: two pointers
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        holder = set(["a","e","i","o","u","A","E","I","O","U"])
        p1 = 0
        p2 = len(s)-1
        while p2 >= p1:
            if s[p1] in holder and s[p2] not in holder:
                p2 -= 1
            elif s[p2] in holder and s[p1] not in holder:
                p1 += 1
            elif s[p1] not in holder and s[p2] not in holder:
                p1 += 1
                p2 -= 1
            else:
                s[p1],s[p2] = s[p2],s[p1]
                p1 += 1
                p2 -= 1
        return "".join(s)
