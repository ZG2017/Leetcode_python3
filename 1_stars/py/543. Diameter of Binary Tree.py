# recursively check the longest path for left and right node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, root):
        if not root:
            return 0
        left_dis = self.recursive(root.left)
        right_dis = self.recursive(root.right)
        if left_dis + right_dis > self.max:
            self.max = left_dis + right_dis
        return max(left_dis, right_dis) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.recursive(root)
        return self.max 