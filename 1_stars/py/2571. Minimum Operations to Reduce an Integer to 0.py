# decimal to binary
# from low digit to high digit, merge continuous '1' by adding 1 at lowest digit that is 1
# if there is only 1 continuous '1' sublist, directly remove it

class Solution:
    def minOperations(self, n: int) -> int:
        bins = list(bin(n)[2:])

        one_c = 0
        for _bin in bins:
            if _bin == '1':
                one_c += 1
        
        i = len(bins)-1
        ans = 0
        while i >= 0:
            if bins[i] == '0':
                i -= 1
            else:
                i -= 1
                c = 1
                while i >= 0 and bins[i] == '1':
                    i -= 1
                    c += 1
                if c == 1: # if only 1 continous '1' sublist, directly remove it
                    ans += 1
                elif i < 0: # hit the highest digit
                    ans += 2
                    break
                else:   # didn't hit the highest digit, carry 1 to next digit and continue 
                    bins[i] = '1'
                    ans += 1
        return ans


            
        return min(one_c, zero_inbetween_c+2)