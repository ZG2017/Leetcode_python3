# mine:
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        p1 = head
        p2_pre = head.next
        p2 = head.next.next
        always_head = head.next
        while p2:
            if p2.next:
                tmp_p2 = p2.next.next
            else: tmp_p2 = None
            tmp_p2_pre = p2.next
            p2_pre.next = p2.next
            p2.next = always_head
            p1.next = p2
            p2 = tmp_p2
            p2_pre = tmp_p2_pre
            p1 = p1.next
        return head
