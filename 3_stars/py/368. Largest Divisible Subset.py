# updated:(dp)
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        nums.sort()
        n = len(nums)
        res = []
        dp = [1 for _ in range(n)]
        saver = {}
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    saver[i] = j
        if max(dp) == 1:
            return [nums[0]]
        index = dp.index(max(dp))
        while index in saver:
            res = [nums[index]] + res
            index = saver[index]
        res = [nums[index]] + res
        return res


# updated:(dp, faster)
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp, n = [[num] for num in nums], len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not nums[j] % nums[i] and len(dp[i]) >= len(dp[j]):
                    dp[j] = dp[i] + [nums[j]]
        dp.sort(key = len)
        return dp and dp[-1]
