# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        tmp_val = head.val
        current_head = head.next
        tmp_front = head
        while current_head:
            if tmp_val == current_head.val:
                tmp_front.next = current_head.next
                current_head = current_head.next
            else:
                tmp_front = current_head
                tmp_val = current_head.val
                current_head = current_head.next
        return head 