# dp

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # corner case
        if sum(nums)%2 != 0:
            return False

        # init
        dp = [[False]*((sum(nums)//2)+1) for i in range(len(nums))]
        for i in range((sum(nums)//2)+1):
            dp[0][i] = True if nums[0] == i else False

        # dp
        for i in range(1, len(nums)):
            for j in range((sum(nums)//2)+1):
                if j-nums[i] <= 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]
