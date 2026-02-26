# assume such operation is possible, then the number of operations x is the number of 1's in the binary representation of num1-(x*num2)

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        x, k=num1, 1
        while True:
            x-=num2
            if x<k: return -1
            if k>=x.bit_count():
                return k
            k+=1
        return -1