# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None
        new = ListNode(0)
        new.next = head
        wait = new
        current = head
        before = new
        while current:
            if current.val < x:
                if before == wait:
                    before = current
                    wait = current
                    current = current.next
                else:
                    before.next = current.next
                    current.next = wait.next
                    wait.next = current
                    wait = wait.next
                    current = before.next
            else:
                before = current
                current = current.next
        return new.next 