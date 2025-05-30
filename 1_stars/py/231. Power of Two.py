# mine:
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)[2:]
        return n == "1" or (n[0] == "1" and all(i == "0" for i in n[1:]))



# updated:
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1:
            if n & 1 == 1:
                return False
            n = n >> 1
        return True


# updated:
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (-n)&n==n and n!=0
