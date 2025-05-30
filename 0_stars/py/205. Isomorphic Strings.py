# mine:
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dit = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] in dit:
                if t[i] != dit[s[i]]:
                    return False
            else:
                if t[i] in mapped:
                    return False
                else:
                    dit[s[i]] = t[i]
                    mapped.add(t[i])
        return True



# updated:
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
