# 2-dimensional dp
# dp[i][0] is the length of the longest increasing subsequence ending at index i
# dp[i][1] is the number of the longest increasing subsequence ending at index i
# dp[i][0] = max(dp[j][0] + 1) for j < i and nums[j] < nums[i]
# dp[i][1] = sum(dp[j][1]) for j < i and nums[j] < nums[i]

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1
        dp = [[-float('inf'), -float('inf')] for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1
        max_length = 0
        for i in range(1, n):
            cur_length_list = []
            cur_n_list = []
            for j in range(0, i):
                if nums[j] < nums[i]:
                    cur_length_list.append(dp[j][0])
                    cur_n_list.append(dp[j][1])
            if len(cur_length_list) != 0:
                pre_length_max = max(cur_length_list)
                pre_n_max = []
                for idx, j in enumerate(cur_n_list):
                    if cur_length_list[idx] == pre_length_max:
                        pre_n_max.append(j)
                dp[i][0] = pre_length_max + 1
                dp[i][1] = sum(pre_n_max)
            else:
                dp[i][0] = 1
                dp[i][1] = 1
            max_length = max(max_length, dp[i][0])

        res = 0
        for i, j in dp:
            if i == max_length:
                res += j
        return res
