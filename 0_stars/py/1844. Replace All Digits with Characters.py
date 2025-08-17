class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)[::-1]
        ans = []
        while len(s_list) >= 2:
            cur_c, cur_d = s_list.pop(), s_list.pop()
            ans.append(cur_c)
            ans.append(self.shift(cur_c, int(cur_d)))
        ans.extend(s_list)
        return ''.join(ans)

    def shift(self, c, d):
        return chr(ord(c)+d)