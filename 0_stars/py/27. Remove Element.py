# mine:

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        for i in range(len(nums)):
            if nums[index] == val:
                nums.append(nums.pop(index))
                length -= 1
            else:
                index += 1
        return length


# updated:

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index=0
        
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index=index+1
        return index
        
