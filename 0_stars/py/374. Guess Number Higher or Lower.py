# mine:
# # The guess API is already defined for you.
# # @param num, your guess
# # @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# # def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1 = 1
        p2 = n
        while p2 >= p1:
            mid = int((p1+p2)/2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                p2 = mid-1
            else:
                p1 = mid+1

        
