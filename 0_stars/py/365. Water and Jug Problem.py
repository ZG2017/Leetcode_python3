# 使用贝祖定理：https://leetcode-cn.com/problems/water-and-jug-problem/solution/shui-hu-wen-ti-by-leetcode-solution/
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        if (x<=0 or y<=0) and (x != z and y != z):
            return False
        tmp = self.helper(x, y)
        if z%tmp == 0:
            return True
        else:
            return False

    def helper(self, a, b):
        if a == 0 or b == 0:
            return 1
        if a>b:
            a,b = b,a
        if b%a == 0:
            return a
        else:
            return self.helper(b%a, a)
