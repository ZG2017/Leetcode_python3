# mine:
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        string = str(x)
        if string[0] == "-":
            minus = True
            start = 1
        else:
            minus = False
            start = 0
        reverseNumber = string[start:][::-1]
        startIndex = 0
        for char in reverseNumber:
            if char == "0":
                startIndex += 1
            else:
                break
        if minus:
            if int("-" + reverseNumber[startIndex:]) < -(2**31):
                return 0
            else:
                return int("-" + reverseNumber[startIndex:])
        else:
            if int(reverseNumber[startIndex:]) > 2**31-1:
                return 0
            else:
                return int(reverseNumber[startIndex:])
