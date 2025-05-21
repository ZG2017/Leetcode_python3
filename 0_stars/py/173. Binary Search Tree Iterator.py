# mine:
# # Definition for a  binary tree node
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        def helper(root):
            if not root:
                return 
            helper(root.right)
            self.stack.append(root.val)
            helper(root.left)
        helper(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

# # Your BSTIterator will be called like this:
# # i, v = BSTIterator(root), []
# # while i.hasNext(): v.append(i.next())
