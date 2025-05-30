class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_ = 0
        mask = 0
        for i in reversed(range(0, 32)):
            mask |= (1<<i)
            tmp = max_|(1<<i)
            s = set()
            for num in nums:
                s.add(num&mask)
            
            for prefix in s:
                if tmp ^ prefix in s:
                    max_ = tmp
                    break
        return max_
