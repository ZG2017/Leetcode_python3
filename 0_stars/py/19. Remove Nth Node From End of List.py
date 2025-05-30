# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:

    def CheckNone(self,enter,n):
        for i in range(n):
            enter = enter.next
        if enter.next == None:
            return True
        else:
            return False

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while tmp.next:
            if self.CheckNone(tmp,n):
                tmp.next = tmp.next.next
                return dummy.next
            else:
                tmp = tmp.next
        return []
