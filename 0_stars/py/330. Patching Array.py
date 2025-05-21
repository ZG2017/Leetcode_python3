# mine:(heap, TLE)
class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        import heapq
        h = []
        counter = 0
        def helper(base,x):
            if not base:
                return
            while base:
                i = base[0]
                heapq.heappush(h,x+i)
                base.pop(0)
                base_cp = base.copy()
                helper(base_cp,x+i)
        helper(nums,0)
        collect = [0]
        for i in range(1,n+1):
            if not h or i != h[0]:
                counter += 1
                print(i)
                tmp_h = h.copy()
                for j in collect+tmp_h:
                    if i+j > n:
                        break
                    heapq.heappush(h,j+i)
            while h and i == h[0]:
                flag = False
                tmp = heapq.heappop(h)
                if not flag:
                    collect += [tmp]
                    flag = True
        return counter


# updated:  (to build n, need[1,2,4,8,...,x], where x is the largest power of 2 less than n)
# see: http://bookshadow.com/weblog/2016/01/27/leetcode-patching-array/
class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        reachable = 1
        index = 0
        c = 0
        while reachable <= n:
            if index < len(nums) and nums[index] <= reachable:
                reachable += nums[index]
                index += 1
            else:
                reachable <<= 1
                c += 1
        return c
