# updated:

# import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        if len(nums1) == 0:
            if len(nums2)%2 == 0:
                mid = (nums2[int((len(nums2)-1+0)/2)] +nums2[int((len(nums2)-1+0)/2)+1])/2
                return mid
            else:
                mid = nums2[int((len(nums2)-1+0)/2)]
                return mid
        if len(nums2) == 0:
            if len(nums1)%2 == 0:
                mid = (nums1[int((len(nums1)-1+0)/2)] +nums1[int((len(nums1)-1+0)/2)+1])/2
                return mid
            else:
                mid = nums1[int((len(nums1)-1+0)/2)]
                
        if nums1[0] >= nums2[-1]:
            nums = nums2 + nums1
            if len(nums)%2 == 0:
                mid = (nums[int((len(nums)-1+0)/2)] +nums[int((len(nums)-1+0)/2)+1])/2
                return mid
            else:
                mid = nums[int((len(nums)-1+0)/2)]
                return mid
        if nums2[0] >= nums1[-1]:
            nums = nums1 + nums2
            if len(nums)%2 == 0:
                mid = (nums[int((len(nums)-1+0)/2)] +nums[int((len(nums)-1+0)/2)+1])/2
                return mid
            else:
                mid = nums[int((len(nums)-1+0)/2)]
                return mid
        '''
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = int(half_len - i)
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: 
                    max_of_left = nums2[j-1]
                elif j == 0: 
                    max_of_left = nums1[i-1]
                else: 
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
            
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0
