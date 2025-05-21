# stack

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        c = 0
        for i in range(len(num)):
            if len(stack) == 0:
                stack.append(num[i])
            else:
                if num[i] >= stack[-1]:
                    stack.append(num[i])
                else:
                    while stack and stack[-1] > num[i] and c < k:
                        c += 1
                        stack.pop()
                    stack.append(num[i])
        while c < k:
            stack.pop()
            c += 1
        if not stack:
            return "0"
        while stack and stack[0] == '0':
            stack.pop(0)
        if not stack:
            return "0"
        else:
            return ''.join(stack) 