# mine:
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        holder = []
        current = head
        while head:
            holder.append(head.val)
            head = head.next
        def helper(nums):
            if nums:
                index = int(len(nums)/2)
                root = TreeNode(nums[index])
                root.left = helper(nums[:index])
                root.right = helper(nums[index+1:])
                return root
        res = helper(holder)
        return res
