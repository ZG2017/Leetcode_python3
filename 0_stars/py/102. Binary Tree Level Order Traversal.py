# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dit = {}
        def helper(root,level):
            if root == None:
                return
            helper(root.left,level+1)
            helper(root.right,level+1)
            if level not in dit:
                dit[level] = []
                dit[level].append(root.val)
            else:
                dit[level].append(root.val)
        helper(root,0)
        return [i for i in dit.values()]
