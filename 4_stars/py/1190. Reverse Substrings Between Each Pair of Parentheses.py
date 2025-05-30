class Solution:
    def reverseParentheses(self, s: str) -> str:
        cache = []
        for i in s:
            if i  == '(':
                cache.append('')
            elif i == ')':
                curr = cache.pop()[::-1]
                if cache:
                    cache.append(cache.pop()+curr)
                else:
                    cache.append(curr)
            else:
                if cache:
                    cache.append(cache.pop() + i)
                else:
                    cache.append(i)
        return cache[-1]
