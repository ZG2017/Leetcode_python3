# mine:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        def helper(root, sums):
            if root.left == None and root.right == None:
                self.res += sums*10 + root.val
            elif root.left == None and root.right != None:
                helper(root.right,sums*10+root.val)
            elif root.right == None and root.left != None:
                helper(root.left, sums*10+root.val)
            else:
                helper(root.left, sums*10+root.val)
                helper(root.right, sums*10+root.val)
        helper(root,0)
        return self.res
        
