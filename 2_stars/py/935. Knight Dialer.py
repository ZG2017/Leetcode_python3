# dp with cache to save space
class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        holder = {
            1: [6,8],
            2: [7,9],
            3: [4,8], 
            4: [0,3,9], 
            5: [], 
            6: [1,7,0], 
            7: [2,6], 
            8: [1,3], 
            9: [2,4], 
            0: [4,6]
        }
        mod = 1e9 + 7
        dp = [1] * 10
        for _ in range(1, n):
            old_dp = []
            for i in range(10):
                tmp = 0
                for j in holder[i]:
                    tmp += dp[j]
                old_dp.append(tmp)
            dp = [i % mod for i in old_dp]
        return int(sum(dp) % mod)
