# mine:
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        if len(candidates) == 1:
            if candidates[0] == target:
                return [candidates]
        candidates = sorted(candidates)
        res = self.find_target(candidates,target,res,tmp)
        return res
        
    def find_target(self,candidates,target,result,each_result):
        if target < candidates[0]:
            if each_result != []:
                each_result.pop()
            return result
        for i in range(len(candidates)):
            if candidates[i] == target:
                each_result.append(candidates[i])
                result.append(each_result.copy())
                each_result.pop()
                if each_result != []:
                    each_result.pop()
                return result
            elif candidates[i] < target:
                each_result.append(candidates[i])
                result = self.find_target(candidates[i:],target-candidates[i],result,each_result)
            else:
                if each_result != []:
                    each_result.pop()
                return result
        if each_result != []:
            each_result.pop()
        return result

# upgraded:

class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return

            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result
