# Memory Limit Exceeded
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        hi, lo, ans = max(nums), min(nums), 0
        holder = [0] * (hi - lo + 1)
        if len(holder) <= 1:
            return 0
        for i in nums:
            holder[i-lo] = 1
        tmp_gap = 0
        for i in holder:
            if i == 1:
                ans = max(ans, tmp_gap+1)
                tmp_gap = 0
            else:
                tmp_gap += 1
        return ans
        
# Bucket Sort
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        hi, lo, ans = max(nums), min(nums), 0
        bsize = (hi - lo) // (len(nums) - 1) or 1
        buckets = [[] for _ in range(((hi - lo) // bsize) + 1)]
        for n in nums:
            buckets[(n - lo) // bsize].append(n)
        currhi = 0
        for b in buckets:
            if not len(b): continue
            prevhi, currlo = currhi or b[0], b[0]
            for n in b: 
                currhi, currlo = max(currhi, n), min(currlo, n)
            ans = max(ans, currlo - prevhi)
        return ans