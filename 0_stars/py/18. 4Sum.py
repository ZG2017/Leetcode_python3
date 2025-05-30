# mine:

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                start_pointer = j+1
                end_pointer = len(nums)-1
                while end_pointer>start_pointer:
                    tmp_sums = nums[i]+nums[j]+nums[start_pointer]+nums[end_pointer]
                    if tmp_sums == target:
                        if [nums[i],nums[j],nums[start_pointer],nums[end_pointer]] in output:
                            end_pointer-=1
                            start_pointer+=1
                        else:
                            output.append([nums[i],nums[j],nums[start_pointer],nums[end_pointer]])
                            end_pointer-=1
                            start_pointer+=1
                    elif tmp_sums > target:
                        end_pointer-=1
                    else:
                        start_pointer+=1
        return output
