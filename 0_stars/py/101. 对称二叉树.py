# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def match(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.match(node1.left, node2.right) and self.match(node1.right, node2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left and root.right and root.left.val == root.right.val:
            return self.match(root.left, root.right)
        else:
            return False
