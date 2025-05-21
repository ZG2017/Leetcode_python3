# 穷举法：
# 1. 每次从candidates中选取两个数字
# 2. 计算两个数字所有可能的结果
# 3. 依次放回candidates中递归计算
# 4. 直到len(candidates)==2，再计算一次所有结果，如果结果中包含24则True, 否则False.
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.helper(nums, 24.0)

    def get_result(self, num1, num2):
        res = set([])
        res.add(num1+num2)
        res.add(num1*num2)
        res.add(num1-num2)
        res.add(num2-num1)
        if num1 != 0.0:
            res.add(num2/num1)
        if num2 != 0.0:
            res.add(num1/num2)
        return res
    
    def helper(self, candidates, target):
        if len(candidates) == 2:
            for k in self.get_result(candidates[0], candidates[1]):
                if abs(k-target) <= 10e-5:
                    return True
        
        for i in range(len(candidates)-1):
            for j in range(i+1, len(candidates)):
                tmp1, tmp2 = candidates[i], candidates[j]
                cur_candidates = candidates[:i] + candidates[i+1:j] + candidates[j+1:]
                tmps = self.get_result(tmp1, tmp2)
                for k in tmps:
                    if self.helper(cur_candidates + [k], target):
                        return True
        return False                



                    

