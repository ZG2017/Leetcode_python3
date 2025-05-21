# mine:
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        m = int(n**0.5)
        holder = [1 for _ in range(n)]
        holder[0] = holder[1] = 0
        tmp = 2
        while tmp <= m:
            if holder[tmp] != 0:
                holder[2*tmp::tmp] = [0]*(int((len(holder)-1)/tmp)-1)
            tmp += 1
        return sum(holder)



# updated:
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i*i:n:i] = [0] * int((n-i*i-1)/i + 1)               
        return sum(s)
