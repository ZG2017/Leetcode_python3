# stack

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for idx, value in reversed(list(enumerate(heights))):
            if len(stack) == 0 or value > stack[-1][1]:
                stack.append((idx, value))
        return [stack[i][0] for i in range(len(stack)-1, -1, -1)]