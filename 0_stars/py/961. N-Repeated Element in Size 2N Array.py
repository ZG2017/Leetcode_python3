class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        visit = set([])
        for i in nums:
            if i in visit:
                return i
            else:
                visit.add(i)
