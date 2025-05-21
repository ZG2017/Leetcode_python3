# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if not cur_node:
                continue
            stack.append(cur_node.left)
            stack.append(cur_node.right)
            if low <= cur_node.val <= high:
                res += cur_node.val
        return res



