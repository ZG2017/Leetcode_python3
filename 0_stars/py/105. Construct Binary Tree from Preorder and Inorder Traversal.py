# mine:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        def helper(preorder,inorder,how_many):
            if inorder == []:
                return None,how_many
            root = TreeNode(preorder[how_many:][0])
            index = inorder.index(preorder[how_many:][0])
            how_many += 1
            root.left, tmp = helper(preorder,inorder[:index],how_many)
            how_many = tmp
            root.right,tmp = helper(preorder,inorder[index+1:],how_many)
            how_many = tmp
            return root,how_many
        
        Root,aaa = helper(preorder,inorder,0)
        return Root


# updated:(recursion nut simpler)
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root


# updated:(stack, very fast)
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    # iterative, stack
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        i, j = 1, 0
        
        while i < len(preorder):
            tmp = None
            node = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                tmp = stack.pop()
                j +=1
            if tmp:
                tmp.right = node
            else:
                stack[-1].left = node
                
            stack.append(node)
            i +=1
            
        return root
