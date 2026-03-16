class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefix_sum_left = [0]
        prefix_sum_right = [0]
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            prefix_sum_left.append(curr)
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            curr += nums[i]
            prefix_sum_right.append(curr)
        prefix_sum_right = prefix_sum_right[::-1]
        
        ans = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            if prefix_sum_left[i] == prefix_sum_right[i+1]:
                ans += 2
            elif abs(prefix_sum_left[i] - prefix_sum_right[i+1]) == 1:
                ans += 1
        return ans
        
        