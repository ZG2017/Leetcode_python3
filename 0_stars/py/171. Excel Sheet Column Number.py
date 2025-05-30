# mine(stupid)
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dit = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,\
               "J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,\
              "T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
        res = 0
        for i in s:
            res *= 26
            res += dit[i]
        return res
            


# updated:  (ord function)
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res *= 26
            res += ord(c) - ord('A') + 1
        return res
