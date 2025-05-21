class Solution:
    def helper(self, x):
        return self.a*x**2 + self.b*x + self.c

    def find_mid_index(self, x, mid_val):
        sp = 0
        ep = len(x)
        while ep > sp+1:
            mid = int((sp + ep)/2)
            if x[mid] <= mid_val:
                sp = mid
            else:
                ep = mid
        return sp


    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        self.a = a
        self.b = b
        self.c = c
        value = list(map(self.helper, nums))
        if a == 0:
            if b > 0:
                return value
            else:
                return value[::-1]
        mid = -b/(2*a)
        reverse = a < 0
        mid_index = self.find_mid_index(nums, mid)
        sp = mid_index
        ep = mid_index + 1
        res = [] 
        for i in range(len(nums)):
            if ep > len(nums)-1:
                res.append(value[sp])
                sp -= 1
                continue
            elif sp < 0:
                res.append(value[ep])
                ep += 1
                continue
            if abs(nums[sp]-mid) > abs(nums[ep]-mid):
                res.append(value[ep])
                ep += 1
            else:
                res.append(value[sp])
                sp -= 1
        if reverse:
            return res[::-1]
        return res
        

    
