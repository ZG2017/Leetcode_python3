# mine: 
# # (a * b) % p = (a % p * b % p) % p
# # a ^ b % p = ((a % p)^b) % p
class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        tmp_a = a
        for n in b[::-1]:
            res = res * (tmp_a**n)%1337
            tmp_a = (tmp_a**10)%1337
        return res%1337
