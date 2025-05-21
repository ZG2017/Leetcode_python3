# mine:
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        import heapq
        n = len(nums1)
        m = len(nums2)
        
        h = [[nums1[0]+nums2[0],0,0]]
        dit = {(0,0):1}
        res = []
        while h and len(res) < k:
            _,x,y = heapq.heappop(h)
            res.append([nums1[x],nums2[y]])
            if x+1 < n and (x+1,y) not in dit:
                heapq.heappush(h,[nums1[x+1]+nums2[y],x+1,y])
                dit[(x+1,y)] = 1
            if y+1 < m and (x,y+1) not in dit:
                heapq.heappush(h,[nums1[x]+nums2[y+1],x,y+1])
                dit[(x,y+1)] = 1
        return res 