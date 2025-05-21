# mine：
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return float(int(num**0.5)) == num**0.5



# updated:  (binary search)
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left = 1
        right = num
        while left <= right:
            mid = (right - left) // 2 + left
            print(mid)
            if num / mid == mid:
                return True
            elif mid < num / mid:
                left = mid + 1
            else:
                right = mid - 1
        return False
