# dfs: TLe
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/867956/python3-two-solutions-dp-with-bit-mask48-bqf0/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or int(sum(nums)/k) != sum(nums)/k:
            return False
        nums.sort(reverse=True)
        parts = [sum(nums)/k]*k
        return self.dfs(parts, nums, 0)
        
    def dfs(self, parts, nums, idx):
        if idx == len(nums):
            return not sum(parts)
        for i in range(len(parts)):
            if parts[i] >= nums[idx]:
                parts[i] -= nums[idx]
                if self.dfs(parts, nums, idx+1):
                    return True
                parts[i] += nums[idx]
        return False

# dp with bitmask

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or int(sum(nums)/k) != sum(nums)/k:
            return False
        
        nums.sort(reverse=True)
        avg = sum(nums)//k
        if nums[0] > avg:
            return False
        
        overall_mask = (1 << len(nums)) - 1

        @cache
        def helper(mask, cur_avg):
            if mask == overall_mask:
                return cur_avg == 0
            holder = []
            for i in range(len(nums)):
                if mask & (1 << i) == 0:
                    tmp_avg = nums[i] + cur_avg
                    if tmp_avg < avg:
                        holder.append(helper(mask | 1 << i, tmp_avg))
                    elif tmp_avg == avg:
                        holder.append(helper(mask | 1 << i, 0))
            return any(holder)
    
        return helper(0, 0)

        
