# mine:(two pointers)
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p1 = 0
        p2 = 0
        mini = float("inf")
        cur_sum = nums[0]
        while p2 < len(nums) and p2>=p1:
            if cur_sum < s:
                if p2 < len(nums)-1:
                    p2 += 1
                    cur_sum += nums[p2]
                else:
                    break
            else:
                if p2-p1+1 < mini:
                    mini = p2-p1+1
                p1 += 1
                cur_sum -= nums[p1-1]
        if mini == float("inf"):
            return 0
        else:
            return mini



# updated:(same but simpler)
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = csum = 0
        n = len(nums)
        ans = n + 1
        
        for i in range(n):
            csum += nums[i]
            
            while csum >= s:
                ans = min(ans, i - left + 1)
                csum -= nums[left]
                left += 1
                
                
        return ans if ans <= n else 0

