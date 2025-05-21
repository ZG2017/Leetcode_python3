# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        input_1 = ""
        input_2 = ""
        while l1:
            input_1 += str(l1.val)
            l1 = l1.next
        while l2:
            input_2 += str(l2.val)
            l2 = l2.next
        res = list(str(int(input_1)+int(input_2))[::-1])

        head = ListNode(res.pop())
        cur_head = head
        while res:
            cur_head.next = ListNode(res.pop())
            cur_head = cur_head.next
        return head


