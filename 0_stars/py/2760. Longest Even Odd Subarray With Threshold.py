class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        for i in range(len(nums)):
            ct = 0
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                ct = 1
                for j in range(i + 1, len(nums)):
                    if (nums[j] % 2 == nums[j - 1] % 2) or nums[j] > threshold:
                        break
                    ct += 1
            ans = max(ans, ct)
        return ans

