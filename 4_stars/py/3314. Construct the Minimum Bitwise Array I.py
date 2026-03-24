# if num is 2, return -1.
# for the rest, the key is to find the first 0 from lower digits to higher digits.

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        final_ans = []
        for num in nums:
            if num == 2:
                final_ans.append(-1)
            else:
                ans = []
                has_zero = False
                cur_bin = bin(num)[2:][::-1]
                for idx, binary in enumerate(cur_bin):
                    if binary == '1':
                        ans.append('1')
                    else:
                        ans.pop()
                        ans.append('0')
                        ans.append('0')
                        has_zero = True
                        break
                if has_zero:
                    ans += cur_bin[idx+1:]
                else:
                    ans = ['1']*(len(ans)-1) + ['0']
                final_ans.append(int(''.join(ans[::-1]), 2))
        return final_ans
            

# updated solution with bit manipulation:class Solution:
def minBitwiseArray(self, nums: List[int]) -> List[int]:
    ans = []

    for num in nums:
        if num % 2 == 0:   # in this problem, only 2 matters, but this is more general
            ans.append(-1)
            continue

        k = 0
        x = num
        while x & 1: # find the first 0 from lower digits to higher digits.
            k += 1
            x >>= 1

        ans.append(num - (1 << (k - 1)))

    return ans