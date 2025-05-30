# mine:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n== 0:
            return []
        memo = {}
        base = [i for i in range(1,n+1)]
        def helper(base):
            if base == []:
                return [None]
            if tuple(base) not in memo:
                nodes = []
                for i in range(len(base)):
                    for j in helper(base[:i]):
                        for k in helper(base[i+1:]):
                            tmp = TreeNode(base[i])
                            tmp.left= j
                            tmp.right= k
                            nodes.append(tmp)
                memo[tuple(base)] = nodes
                return nodes
            else:
                return memo[tuple(base)]
        res = helper(base)
        return res 
