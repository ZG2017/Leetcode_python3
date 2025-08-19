class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = 0
        cur = 0
        for i in gain:
            cur += i
            ans = max(cur, ans)
        return ans