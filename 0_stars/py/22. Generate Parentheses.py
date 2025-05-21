# mine:

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        base = []
        output = []
        flag = [False]*(n)
        for i in range(n):
            base.append(i)
        while True:
            output.append(self.build(base,n))
            if sum(base) >= (n-1)*n:
                break
            base[-1] += 1
            if base[-1]>(n-1)*2:
                for i in range(n-1,0,-1):
                    if base[i] >i*2:
                        base[i-1] += 1
                        flag[i] = True
                    for j in range(2,len(flag)):
                        if flag[j]:
                            base[j] = base[j-1]+1
                flag = [False]*(n)
        return output
    
    def build(self,nums,n):
        strs = list(")"*2*n)
        for i in nums:
            strs[i] = "("
        return "".join(strs)

# updated:

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        left = right = n
        result = []
        self.generate(left, right, result, '')
        return result
    def generate(self, left, right, result, string):
        if left == 0 and right == 0:
            result.append(string)
            return
        if left:
            self.generate(left - 1, right , result, string+'(')
        if left < right:
            self.generate(left, right - 1, result, string+')')
