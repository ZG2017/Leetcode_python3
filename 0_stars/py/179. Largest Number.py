# mine:(not correct)
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(i) for i in nums]
        nums_cp = nums.copy()
        max_len = max([len(i) for i in nums])
        for i in range(len(nums)):
            for j in range(max_len-len(nums[i])):
                nums[i] += nums[i][-1]
        tmp = []
        for i,j in enumerate(nums):
            tmp.append((j,i))
        tmp = sorted(tmp,key = lambda x:x[0],reverse = True)
        res = ""
        for i in tmp:
            res += nums_cp[i[1]]
        return str(int(res))


# updated:
# from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
    def largestNumber(self, nums):
        sorted_nums = sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
        result = ''.join(sorted_nums)
        return str(int(result))


# updated:
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        longest = max([len(x) for x in nums], default=0)
        nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
        if nums and nums[0] == '0':
            return '0'
        return ''.join(nums)
