# recursive solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        is_bst, _max, _min, size = self.check_bst(root)
        return size

    def check_bst(self, root):
        """is_bst, max, min, size"""
        if not root.left and not root.right:
            return True, root.val, root.val, 1
        elif root.left and not root.right:
            is_bst, _max, _min, size = self.check_bst(root.left)
            is_bst = (root.val > _max) & is_bst
            if is_bst:
                return True, root.val, _min, size + 1
            else:
                return False, 0, 0, size
        elif root.right and not root.left:
            is_bst, _max, _min, size = self.check_bst(root.right)
            is_bst = (root.val < _min) & is_bst
            if is_bst:
                return True, _max, root.val, size + 1
            else:
                return False, 0, 0, size
        else:
            is_bst_l, _max_l, _min_l, size_l = self.check_bst(root.left)
            is_bst_r, _max_r, _min_r, size_r = self.check_bst(root.right)
            is_bst_root = _max_l < root.val < _min_r
            is_bst = is_bst_root & is_bst_l & is_bst_r
            if is_bst:
                return True, _max_r, _min_l, size_l + size_r + 1
            else:
                return False, 0, 0, max(size_l, size_r)
