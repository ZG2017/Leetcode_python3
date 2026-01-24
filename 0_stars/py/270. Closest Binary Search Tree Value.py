# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return -1
        if target == root.val:
            return root.val
        elif target < root.val:
            closest = self.closestValue(root.left, target)
        else:
            closest = self.closestValue(root.right, target)
        
        if closest == -1:
            return root.val
        elif abs(root.val-target) == abs(closest-target):
            return min(root.val, closest)
        elif abs(root.val-target) < abs(closest-target):
            return root.val
        else:
            return closest
