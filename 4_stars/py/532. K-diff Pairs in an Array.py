# hashmap
# only need to go througth once for checking whether a+k in the hashmap since a-k is covered at 'a-k'-th checking for (a-k)+k

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        holder = Counter(nums)
        res = 0
        if k == 0:
            for i in holder.values():
                if i > 1:
                    res += 1
            return res
        for i in holder:
            if i + k in holder:
                res += 1
        return res
