# mine:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            index = int(len(nums)/2)
            root = TreeNode(nums[index])
            root.left = self.sortedArrayToBST(nums[:index])
            root.right = self.sortedArrayToBST(nums[index+1:])
            return root
