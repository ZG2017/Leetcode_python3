class Solution:
    def minimumPairRemoval(self, nums):
        operations = 0

        while not self.is_non_decreasing(nums):
            min_sum = nums[0] + nums[1]
            index = 0

            for i in range(1, len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    index = i

            nums[index] = min_sum
            nums.pop(index + 1)
            operations += 1

        return operations

    def is_non_decreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True