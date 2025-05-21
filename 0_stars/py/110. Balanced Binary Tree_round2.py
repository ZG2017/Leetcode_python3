# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def helper(self, root):
        if not root:
            return 0, True
        left = 0
        left_state = True
        right = 0
        right_state = True
        if root.left:
            left, left_state = self.helper(root.left)
        if root.right:
            right, right_state = self.helper(root.right)
        if left_state and right_state and abs(left-right) <= 1:
            return max(left, right)+1, True
        else:
            return max(left, right)+1, False
                
    def isBalanced(self, root: TreeNode) -> bool:
        _, res = self.helper(root)
        return res
