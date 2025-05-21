# Floyd's Cycle-Finding algorithm:
# 1. Faster and slower pointer until meetup. faster pointer is twice as fast as slower one
# 2. Reset the slower pointer to the head, same pace until meetup.
# 3. return either slower and faster pointer.

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return None
        p1 = head
        p2 = head
        p1 = p1.next
        p2 = p2.next.next
        while p2:
            if p1 == p2:
                p1 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
            p1 = p1.next
            if p2.next == None:
                return None
            p2 = p2.next.next
        return None


