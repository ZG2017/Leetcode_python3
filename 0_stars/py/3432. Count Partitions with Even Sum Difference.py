# prefix sum
class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_sum_from_left = []
        cur_sum = 0
        for i in nums:
            cur_sum += i
            pre_sum_from_left.append(cur_sum)
        
        pre_sum_from_right = []
        cur_sum = 0
        for i in nums[::-1]:
            cur_sum += i
            pre_sum_from_right.append(cur_sum)
        pre_sum_from_right = pre_sum_from_right[::-1]

        ans = 0
        for i in range(1, len(nums)):
            if (pre_sum_from_left[i-1] - pre_sum_from_right[i]) %2 == 0:
                ans += 1
        return ans