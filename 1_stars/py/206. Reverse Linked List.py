# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    def reverseList(self, head):
        if not head:
            return None
        tmp_head = head
        pre = head
        cur = head.next
        while cur:
            tmp = cur.next
            pre.next = cur.next
            cur.next = tmp_head
            tmp_head = cur
            cur = tmp
        return tmp_head
    """
    def reverseList(self, head):
        if not head or not head.next:
            return head
        def helper(head):
            if head.next == None:
                return head,head
            tmp_head,tail = helper(head.next)
            head.next = None
            tail.next = head
            return tmp_head,head
        res,_ = helper(head)
        return res

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre 