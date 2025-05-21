# mine: (take too much time)
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(s):
            stack = []
            for i in range(len(s)):
                if not stack and s[i] == ")":
                    return False
                elif s[i] not in "()":
                    continue
                elif s[i] == "(":
                    stack.append(s[i])
                elif s[i] == ")" and stack[-1] == "(":
                    stack.pop()
            if not stack:
                return True
            else:
                return False
        
        res = []
        found_len = 0
        total_stack = [s]
        while total_stack and len(total_stack[0]) >= found_len:
            tmp = total_stack.pop(0)
            c = tmp.count("(") - tmp.count(")") 
            if tmp and (tmp[0] == ")" or tmp[-1] == "("):
                for i in range(len(tmp)):
                    if c > 0 and tmp[i] == ")" or c < 0 and tmp[i] == "(" or (tmp[:i]+tmp[i+1:] in total_stack):
                        continue
                    total_stack.append(tmp[:i]+tmp[i+1:])
            elif valid(tmp):
                found_len = len(tmp)
                if tmp not in res:
                    res.append(tmp)
            else:
                for i in range(len(tmp)):
                    if c > 0 and tmp[i] == ")" or c < 0 and tmp[i] == "(" or (tmp[:i]+tmp[i+1:] in total_stack):
                        continue
                    total_stack.append(tmp[:i]+tmp[i+1:])
        return res



# updated: (unread)
class Solution:
    def removeInvalidParentheses(self, s):
        result = []
        self.helper(s, ['(', ')'], result, 0, 0)
        return result
        
    def helper(self, s, brackets, result, previousi, previousj):
        count = 0
        for i in range(previousi, len(s)):
            l = s[i]
            if l ==  brackets[0]:
                count += 1
            if l ==  brackets[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(previousj, i+1):
                if s[j] == brackets[1] and (j == previousj or s[j-1] != brackets[1]):
                    self.helper(s[0:j] + s[j+1:], brackets, result, i, j)
            return
        sreversed = s[::-1]
        if brackets[1] == ')':
            self.helper(sreversed, [')','('], result, 0, 0)
        else:
            result += [sreversed]
