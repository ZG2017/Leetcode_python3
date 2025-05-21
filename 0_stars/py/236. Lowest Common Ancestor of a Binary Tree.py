# mine:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.finded = None
        s = (p.val,q.val)
        def helper(root):
            if not root:
                return False
            tmp = False
            if root.val in s:
                tmp = True
            left = helper(root.left)
            right = helper(root.right)
            if (tmp and left and not self.finded)\
            or (tmp and right and not self.finded)\
            or (left and right and not self.finded):
                self.finded = root
                print(1)
            return tmp or left or right
        helper(root)
        return self.finded
