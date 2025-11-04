# https://leetcode.com/problems/house-robber-iv/solutions/6537753/binary-search-visualization-math-python-26vxz/
# mini-max problem
# binary search to find the minimum capability
# in canRob, we need to check if we can rob at least k houses with the given current minimum capability

class Solution(object):
    def canRob(self, nums, mid, k):
        count = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= mid:
                count += 1
                i += 1
            i += 1
        return count >= k

    def minCapability(self, nums, k):
        left, right = 1, max(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if self.canRob(nums, mid, k):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans