# mine:(stupid)
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        dit = {}
        maxs = 0
        val = 0
        for i in range(len(nums)):
            if nums[i] not in dit:
                dit[nums[i]] = 0 
            dit[nums[i]] += 1
            if dit[nums[i]] > maxs:
                maxs = dit[nums[i]]
                val = nums[i]
        return val


# updated:(wonderful)
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        return nums[len(nums) // 2]
