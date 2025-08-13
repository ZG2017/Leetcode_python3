# priority queue
class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        import heapq
        holder = dict()
        ans = []
        q = []
        for v, f in zip(nums, freq):
            holder[v] = holder.get(v, 0) + f
            heapq.heappush(q, (-holder[v], v))
            while q:
                c, v = -q[0][0], q[0][1]
                if c == 0 or holder[v] != c:
                    heapq.heappop(q)
                else:
                    ans.append(c)
                    break
            if len(q) == 0:
                ans.append(0)
        return ans
        