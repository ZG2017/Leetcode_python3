class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = []
        T = T[::-1]
        for idx,i in enumerate(T):
            while stack and T[stack[-1]] <= i:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(idx-stack[-1])
            stack.append(idx)
        return res[::-1]

