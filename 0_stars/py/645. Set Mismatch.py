# math and for loop 

# O(n)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        expect_sum = (len(nums)*(len(nums)+1))//2
        cur_sum = sum(nums)
        a_b = expect_sum - cur_sum

        holder = [0]*len(nums)
        for i in nums:
            if holder[i-1] != 0:
                a = i
                break
            else:
                holder[i-1] = i
        return [a, a+a_b]
        
