# mine:
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        tmp_c = 1
        c = 0
        for _ in range(1,len(nums)):
            if nums[index] == nums[index-1]:
                tmp_c +=1
                if tmp_c > 2:
                    nums.append(nums.pop(index))
                    c += 1 
                    index -= 1
            else:
                tmp_c = 1
            index += 1
        
        return len(nums)-c

# updated:
# class Solution
#     def removeDuplicates(self, nums)
#         
#         type nums List[int]
#         rtype int
#         
#         n=0
#         for i in nums
#             if n2 or inums[n-2]
#                 nums[n]=i
#                 n +=1
#         return n 