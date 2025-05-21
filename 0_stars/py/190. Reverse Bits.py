# mine:
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        tmp = str(bin(n))[2:]
        tmp = "0"*(32-len(tmp))+tmp
        tmp = tmp[::-1]
        return int(tmp,2)
