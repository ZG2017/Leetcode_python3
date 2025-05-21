# 动态规划：dp[i][j]表示从i到j， A玩家在区间[i, j]能拿到的最大值， B玩家能拿到的最大值则根据flag从dp[1][len(nums)-1]或者dp[0][len(nums)-2]中选择其一
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(0, len(nums)-1):
            dp[i][i+1] = max(nums[i], nums[i+1])
            dp[i][i] = nums[i]
        dp[len(nums)-1][len(nums)-1] = nums[-1]
        flag = True

        for ws in range(2, len(nums)):
            for i in range(0, len(nums)-ws):
                tmp1 = nums[i] + min(dp[i+2][i+ws], dp[i+1][i+ws-1])
                tmp2 = nums[i+ws] + min(dp[i][i+ws-2], dp[i+1][i+ws-1])
                if tmp1 > tmp2:
                    flag = True
                    tmp = tmp1
                else:
                    flag = False
                    tmp = tmp2
                dp[i][i+ws] = tmp
        #print(dp)
        if flag: 
            return dp[0][len(nums)-1] >= dp[1][len(nums)-1]
        else:
            return dp[0][len(nums)-1] >= dp[0][len(nums)-2]

