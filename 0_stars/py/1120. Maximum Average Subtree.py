# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def average(self, root):
        if not root:
            return 0, 0
        left_total, left_node = 0, 0
        right_total, right_node = 0, 0
        if root.left:
            left_total, left_node = self.average(root.left)
        if root.right:
            right_total, right_node = self.average(root.right)
        left_average = left_total/left_node if left_node != 0 else 0
        right_average = right_total/right_node if right_node != 0 else 0
        cur_average = (left_total + right_total + root.val)/(left_node + right_node + 1)
        self.holder = max(self.holder, cur_average, left_average, right_average)
        return left_total + right_total + root.val, left_node + right_node + 1

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0
        self.holder = -1
        self.average(root)
        return self.holder
        
