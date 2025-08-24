# dp (TLE)

class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        holder = dict()
        ans = 2
        holder[0] = {0:1}
        for i in range(1, len(nums)):
            cur_num = nums[i]
            holder[i] = dict()
            for j in range(0, i):
                pre_num = nums[j]
                cur_dis = cur_num - pre_num
                if cur_dis not in holder[i]:
                    holder[i][cur_dis] = 2
                for dis in holder[j]:
                    if cur_dis == dis:
                        holder[i][cur_dis] = holder[j][cur_dis] + 1
                        if holder[i][cur_dis] > ans:
                            ans = holder[i][cur_dis]
        return ans


# dp: notice the inner most for lopp is not necessary, so give up the inner most for loop
class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        holder = dict()
        ans = 2
        holder[0] = {0:1}
        for i in range(1, len(nums)):
            cur_num = nums[i]
            holder[i] = dict()
            for j in range(0, i):
                pre_num = nums[j]
                cur_dis = cur_num - pre_num
                holder[i][cur_dis] = holder[j].get(cur_dis, 1) + 1
                if holder[i][cur_dis] > ans:
                    ans = holder[i][cur_dis]
        return ans
