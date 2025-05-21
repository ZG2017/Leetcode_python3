# mine:
class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return True
        tmp = []
        while data:
            tmpChar = data[0]
            c = 0
            if tmpChar < 128:
                c = 0
            elif tmpChar >= 128 and tmpChar < 128+64:
                c = 1
            elif tmpChar >= 128+64 and tmpChar < 128+64+32:
                c = 2
            elif tmpChar >= 128+64+32 and tmpChar < 128+64+32+16:
                c = 3
            elif tmpChar >= 128+64+32+16 and tmpChar < 128+64+32+16+8:
                c = 4
            else:
                return False
            if c == 1: return False
            elif c == 0:
                data = data[c+1:]
                continue
            else:
                tmp, data = data[1:c], data[c:]
            if len(tmp) != c-1:
                return False
            for i in tmp:
                if i <= 192 and i >= 128:
                    continue
                else:
                    return False
        return True


# updated:(binary computation)
class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for num in data:
            if not count:
                if (num >> 5) == int('110', 2):
                    count = 1
                elif (num >> 4) == int('1110', 2):
                    count = 2
                elif (num >> 3) == int('11110', 2):
                    count = 3
                elif (num >> 7): # No leading byte and num is not a 1-byte character
                    return False
            else:
                if num >> 6 != int('10', 2):
                    return False
                
                count -= 1
            
        return count == 0
