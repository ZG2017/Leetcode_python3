class Solution:
    def findNthDigit(self, n: int) -> int:
        bits_per_num = 1
        time = 1
        cur_bit = 0  
        pre_bit = 0
        base = 9
        cur_init_num = 1
        while  n > cur_bit:
            pre_bit = cur_bit
            cur_bit += bits_per_num*base*time
            cur_init_num = 10**(bits_per_num-1)
            time *= 10
            bits_per_num += 1
        final_bits_per_num = bits_per_num - 1
        tmp = math.ceil((n - pre_bit)/(final_bits_per_num))-1
        final_num = cur_init_num + tmp
        n_remain = (n - pre_bit) - final_bits_per_num * tmp
        final_bit = int(str(final_num)[n_remain-1])
        return final_bit


# # same ieda but better function
class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 9
        cur_sum = base
        pre_sum = 0
        # i 为数字位数
        for i in range(1, 100000):
            if n <= cur_sum:
                div, mod = divmod(n - pre_sum - 1, i)
                num = 10 ** (i-1) + div
                return int(str(num)[mod])
            
            
            base = (10 ** (i)) * (i + 1) * 9
            pre_sum = cur_sum
            cur_sum += base
