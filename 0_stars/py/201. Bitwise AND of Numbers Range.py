# 观察到2进制的0和1是有周期性的，探查周期性质就能判断按位AND的结果是0还是1
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if n == 0:
            return 0
        diff = n-m
        if diff == 0:
            return n
        num_bit = math.ceil(math.log2(n))
        holder = [0]*num_bit
        res = 0
        for i in range(num_bit):
            base = 2**i
            if diff//base >= 1:
                holder[i] = 0
            elif m//base != n//base:
                holder[i] = 0
            elif m//base%2 == 0:
                holder[i] = 0
            else:
                holder[i] = 1
            res += base if holder[i] == 1 else 0
        return res

