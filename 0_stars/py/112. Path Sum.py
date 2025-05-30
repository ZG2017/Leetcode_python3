# mine:（dfs）
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.flag = False
        def helper(root,sums):
            if root:
                if sums-root.val == 0 and not root.left and not root.right:
                    self.flag = True
                helper(root.left,sums-root.val)
                helper(root.right,sums-root.val)
        
        helper(root,sum)
        return self.flag
            


# updated:  (same but in simpler expression)
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if ((not root.left) and (not root.right)):
            return sum == root.val
        
        return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)
