# fast and slow pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p1, p2 = head, head
        if not head.next:
            return False
        while p1 and p2:
            if not p1.next:
                return False
            elif not p2.next or not p2.next.next:
                return False
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False 