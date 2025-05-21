# mine:(naive dp, TLE)
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort()
        n = len(envelopes)
        dp = [1 for _ in range(n)]
        index = 0
        while index < n:
            tmp = 0
            while envelopes[tmp][0] < envelopes[index][0]:
                if envelopes[tmp][1] < envelopes[index][1]:
                    dp[index] = max(dp[index],dp[tmp]+1)
                tmp += 1
            index += 1
        return max(dp)


# mine:(binary search, dp, still TLE)
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort()
        n = len(envelopes)
        dp = [1 for _ in range(n)]
        saver = {}
        keys = []
        index = 0
        res = 1
        while index < n:
            for i in keys:
                if i < envelopes[index][0]:
                    tmp = envelopes[index][1]
                    p1 = saver[i][0]
                    p2 = saver[i][1]
                    while p2 >= p1:
                        mid = int((p1+p2)/2)
                        if envelopes[mid][1] >= tmp:
                            p2 = mid - 1
                        else:
                            p1 = mid + 1
                    for j in range(saver[i][0],p1):
                        dp[index] = max(dp[index],dp[j]+1)
                        res = max(dp[index],res)
                else:
                    break
            if envelopes[index][0] not in saver:
                saver[envelopes[index][0]] = [index,index-1]
                keys.append(envelopes[index][0])
            saver[envelopes[index][0]][1] += 1
            index += 1
        return res


# updated(reference to 300. Longest Increasing Subsequence: sort width and find LIS of heights)
# attention: this code works for python2.0 but not for python3.0
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums = sorted(envelopes, cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = int((low + high) / 2)
                if dp[mid][1] < nums[x][1]:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < len(dp):
                dp[low] = nums[x]
            else:
                dp.append(nums[x])
        return len(dp)
