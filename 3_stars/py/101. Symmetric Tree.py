# mine: thinking too much
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        def recursion(root):
            if root == None:
                return ["None"]
            left = recursion(root.left)
            right = recursion(root.right)
            return [root.val]+left+right
        
        def flip(root):
            if root.left == None and root.right == None:
                return
            elif root.left == None and root.right != None:
                flip(root.right)
                root.left, root.right = root.right, None
            elif root.left != None and root.right == None:
                flip(root.left)
                root.left, root.right = None, root.left
            else:
                flip(root.left)
                flip(root.right)
                root.left, root.right = root.right, root.left
            
        res1 = recursion(root)
        flip(root)
        res2 = recursion(root)
        return res1 == res2


# updated:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymRecus(root.left, root.right)
    
    def isSymRecus(self, left, right):
        if not left and not right:
            return True 
        if (left and not right) or (not left and right):
            return False 
        
        if left.val != right.val:
            return False
        
        return self.isSymRecus(left.left, right.right) and self.isSymRecus(left.right, right.left)
