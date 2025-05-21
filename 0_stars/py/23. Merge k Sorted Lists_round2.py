# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# # divide and conquer 
class Solution:
    def split(self, head):
        if not head:
            return None
        p1 = head
        p2 = head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        second_head = p1.next
        p1.next = None
        return head, second_head

    def merge(self, head1, head2):
        if not head1:
            return head2
        elif not head2:
            return head1
        p1 = head1
        p2 = head2
        dummy_head = ListNode(0)
        cur_head = dummy_head
        while p1 or p2:
            if not p1:
                cur_head.next = p2
                break
            if not p2:
                cur_head.next = p1
                break
            if p1.val < p2.val:
                cur_head.next = p1
                cur_head = cur_head.next
                p1 = p1.next
            else:
                cur_head.next = p2
                cur_head = cur_head.next
                p2 = p2.next
        return dummy_head.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        elif len(lists) == 1:
            head = self.merge(lists[0], ListNode(-float("inf")))
            return head.next
        holder1 = lists[::2]
        holder2 = lists[1::2]
        if len(holder1) != len(holder2):
            tmp = [self.merge(*i) for i in zip(holder1[:-1], holder2)] + [holder1[-1]]
        else:
            tmp = [self.merge(*i) for i in zip(holder1, holder2)]
        res = self.mergeKLists(tmp)
        return res
