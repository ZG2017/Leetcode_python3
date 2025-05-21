# """
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)
"""
class Solution:
    def fib(self, N: int) -> int:
        holder = {0:0,1:1}
        for i in range(2, N+1):
            holder[i] = holder[i-1]+holder[i-2]
        return holder[N]
