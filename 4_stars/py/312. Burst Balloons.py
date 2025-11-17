# bottom up dp with bitmask and memoization

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        def check_zero(mask, idx):
            return mask & (1 << idx) == 0

        def find_near_zero(mask, idx):
            # return left_zero_idx, right_zero_idx
            left, right = 0, 0
            # for left
            for cur_idx in range(idx+1, n):
                if check_zero(mask, cur_idx):
                    left = cur_idx
                    break
            # for right
            for cur_idx in range(idx-1, -1, -1):
                if check_zero(mask, cur_idx):
                    right = cur_idx
                    break
            return left, right

        @cache
        def helper(mask):
            if mask.bit_count() == n-2:
                return 0
            holder = []
            for idx in range(1, n-1):
                if check_zero(mask, idx):
                    left_zero_idx, right_zero_idx = find_near_zero(mask, idx)
                    cur_value = nums[left_zero_idx] * nums[right_zero_idx] * nums[idx]
                    cur_overall_value = cur_value + helper(mask | (1 << idx))
                    holder.append(cur_overall_value)
            return max(holder)
        
        # get ans
        return helper(0)



# updated: top down dp with interval
# https://leetcode.com/problems/burst-balloons/solutions/7162687/interval-dynamic-programming-with-clear-3a6c8/
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in nums if i > 0] + [1]  # 清除为0的数字，因为0不会得分，然后首尾添加[1],方便计算
        n = len(nums)
        dp = [[0] * n for _ in range(n)]  # 初始化dp
        for k in range(2, n):  # k 确定一个滑动窗口的大小，从2开始
            for left in range(0, n - k):  # 滑动窗口，从左向右滑动，确定区间的开始（left）、结束（right）位置
                right = left + k
                for i in range(left + 1, right):  # 开始枚举，区间内哪一个数字作为最后一个被戳破，使其得分最高
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
