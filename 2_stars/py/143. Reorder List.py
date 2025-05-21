# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast = head
        slow = head
        pre = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if fast.next != None:
            tmp = slow.next
            fast = fast.next
            slow.next = None
            slow = tmp
        else:
            pre.next = None
        cur = slow.next
        slow.next = None
        pre = slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        
        node1 = head
        node2 = pre
        while node1.next and node2.next:
            tmp1 = node1.next
            tmp2 = node2.next
            node1.next = node2
            node2.next = tmp1
            node1,node2 = tmp1,tmp2
        if node1 != node2:
            node1.next = node2
