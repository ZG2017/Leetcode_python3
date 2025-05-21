# updated:
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total_area = abs(C-A)*abs(D-B)+abs(G-E)*abs(H-F)
        x1 = max(A,E)
        x2 = min(C,G)
        x = max(x2-x1,0)
        y1 = max(B,F)
        y2 = min(D,H)
        y = max(y2-y1,0)
        return total_area - x*y
