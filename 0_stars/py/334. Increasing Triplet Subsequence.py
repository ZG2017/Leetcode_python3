# mine:  dp, TLE
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[i]+1,dp[j])
                    if dp[j] >= 3:
                        return True
        return False

# udpated: nlogn, binary search
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #import bisect
        if len(nums)<3:
            return False
        saver = []
        for i in range(len(nums)):
            lower = 0
            higher = len(saver)-1
            while lower <= higher:
                mid = int((lower+higher)/2)
                if saver[mid] < nums[i]:
                    lower = mid+1
                elif saver[mid] > nums[i]:
                    higher = mid-1
                else:
                    lower = mid
                    break
            index = lower
            #index = bisect.bisect_left(saver,nums[i])
            if index >= len(saver):
                saver.append(nums[i])
            else:
                saver[index] = nums[i]
            if len(saver) >= 3:
                return True
        return False






