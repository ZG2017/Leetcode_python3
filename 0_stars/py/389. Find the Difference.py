# mine:
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tmp_1 = set(s)
        tmp_2 = set(t)
        if tmp_1 == tmp_2:
            dit_s = {}
            dit_t = {}
            for i in s:
                if i not in dit_s:
                    dit_s[i] = 0
                dit_s[i] += 1
            for i in t:
                if i not in dit_t:
                    dit_t[i] = 0
                dit_t[i] += 1
            for i in dit_s:
                if dit_s[i] != dit_t[i]:
                    return i
        else:
            return str(list(tmp_2-tmp_1)[0])



# updated:
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        memo = [0] * 26
        for c in t:
            memo[ord(c) - ord('a')] += 1
        for c in s:
            memo[ord(c) - ord('a')] -= 1
        for pos, val in enumerate(memo):
            if val > 0:
                return chr(ord('a') + pos)
