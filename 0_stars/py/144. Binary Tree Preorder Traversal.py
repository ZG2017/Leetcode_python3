# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if root == None:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res


# updated:
# updated: (stack)
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        res=[]
        stack=[]
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            else:
                root=stack.pop().right
        return res
