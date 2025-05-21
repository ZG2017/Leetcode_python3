# mine:
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list1 = nums.copy()
        self.list2 = nums.copy()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.list1

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        random.shuffle(self.list2)
        return self.list2


# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.reset()
# # param_2 = obj.shuffle()


# updated:
# import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return sorted(self.nums, key = lambda x: random.random())
