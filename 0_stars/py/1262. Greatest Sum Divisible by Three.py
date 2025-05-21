# greedy
# ref: https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/1813430/Python3-Greedy-Linear-Time

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total%3 == 0:
            return total
        
        holder_1 = [10001, 10002]
        holder_2 = [10001, 10002]
        for num in nums:
            if num%3 == 1:
                if num<holder_1[0]:
                    holder_1[0], holder_1[1] = num, holder_1[0]
                elif num<holder_1[1]:
                    holder_1[1] = num
            elif num%3 == 2:
                if num<holder_2[0]:
                    holder_2[0], holder_2[1] = num, holder_2[0]
                elif num<holder_2[1]:
                    holder_2[1] = num
        
        if total%3 == 1:
            return max(total-holder_1[0], total-sum(holder_2))
        elif total%3 == 2:
            return max(total-holder_2[0], total-sum(holder_1))
        
            
        
        
                
        
