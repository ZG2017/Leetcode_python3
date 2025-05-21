# updated: 
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        res = "0"
        dit = {}
        visited = {}
        for c in s:
            if c not in dit:
                dit[c] = 0
                visited[c] = False
            dit[c] += 1
        
        for c in s:
            dit[c] -= 1
            while c < res[-1] and dit[res[-1]] != 0 and visited[c] == False:
                visited[res[-1]] = False
                res = res[:-1]
            if not visited[c]:
                res += c
                visited[c] = True
        return res[1:]
