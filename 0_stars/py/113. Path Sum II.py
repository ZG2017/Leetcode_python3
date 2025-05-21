# mine:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(root,sums,base):
            if root:
                if sums-root.val == 0 and not root.left and not root.right:
                    res.append(base + [root.val])
                helper(root.left,sums-root.val,base+[root.val])
                helper(root.right,sums-root.val,base+[root.val])
        
        helper(root,sum,[])
        return res
