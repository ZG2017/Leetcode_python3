# mine: time comsuming
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1 = []
        for i in nums:
            if i in l1:
                l1.remove(i)
            else:
                l1.append(i)
        return l1[0]



# updated:
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)
