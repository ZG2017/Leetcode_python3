# mine:
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp_1 = set(nums1)
        tmp_2 = set(nums2)
        return list(tmp_1&tmp_2)
