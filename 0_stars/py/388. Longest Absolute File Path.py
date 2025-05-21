# mine:
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        direct = input.split("\n")
        stack = []
        res = 0
        while direct:
            tmp = direct.pop(0)
            c = 0
            while tmp[0] == "\t":
                c += 1
                tmp = tmp[1:]
            if stack and c <= stack[-1][1]:
                while stack and c <= stack[-1][1]:
                    stack.pop()
            stack.append((tmp,c))
            if "." in tmp:
                tmp_res = "/".join([i[0] for i in stack])
                if len(tmp_res) >= res:
                    res = len(tmp_res)
        return res
