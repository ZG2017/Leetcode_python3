# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return max(self._rob(root))

    def _rob(self, root):
        if not root:
            return 0, 0
        yl, nl = self._rob(root.left)
        yr, nr = self._rob(root.right)
        if root.left and not root.right:
            return root.val + nl, max(yl, nl)
        elif root.right and not root.left:
            return root.val + nr, max(yr, nr)
        elif not root.left and not root.right:
            return root.val, 0
        else:
            return root.val + nl + nr, max([yl + yr, yl + nr, nl + yr, nl + nr])
