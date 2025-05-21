# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        tmp_1 = 0
        tmp_2 = 0
        if not p1 or not p2:
            return None
        while True:
            if tmp_1 >= 2 or tmp_2 >= 2:
                return None
            
            if p1 and p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

            if not p1:
                p1 = headB
                tmp_1 += 1
            if not p2:
                p2 = headA
                tmp_2 += 1
