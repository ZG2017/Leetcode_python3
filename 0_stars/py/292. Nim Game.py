# mine:
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0

# dp dp[i] means whether the player can win the game if there are i stones left in this round.

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        win = [False]*(max(4, n+1)) 
        win[1] = True
        win[2] = True
        win[3] = True
        for i in range(4, n+1):
            win[i] = (not win[i-1]) or (not win[i-2]) or (not win[i-3])
        return win[n]