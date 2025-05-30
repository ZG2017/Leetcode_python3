# mine: (take too much time)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        unique_nums = list(set(nums))
        res = [[-1,-1]] # [times,num]
        dit = {}
        for i in unique_nums:
            tmp = nums.count(i)
            dit[i] = tmp
            p1 = 0
            p2 = len(res)-1
            while p2 >= p1:
                mid = int((p1+p2)/2)
                if res[mid][0] < tmp:
                    p1 = mid+1
                else:
                    p2 = mid-1
            res.insert(p1,[tmp,i])
            if len(res) == k+1:
                res.pop(0)
        return [i[1] for i in reversed(res)]


# mine: nlogn
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dit = {}
        for i in nums:
            if i not in dit:
                dit[i] = 0
            dit[i] += 1
        return [i[0] for i in sorted(dit.items(), key = lambda x: x[1], reverse = True)][:k]
