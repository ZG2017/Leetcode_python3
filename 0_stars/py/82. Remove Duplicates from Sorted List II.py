# mine:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        current_head = head.next
        tmp = head.val
        saver = [0]
        index = 1
        while current_head:
            if current_head.val == tmp:
                saver[index-1] = 1
                saver.append(1)
                tmp = current_head.val
                current_head = current_head.next
                index += 1
            else:
                saver.append(0)
                index += 1
                tmp = current_head.val
                current_head = current_head.next
        index = 0
        new_node = ListNode(0)
        new_node.next = head
        
        current_head = head
        tmp_node = new_node
        while index < len(saver):
            if saver[index] == 0:
                tmp_node = current_head
                current_head = current_head.next
            else:
                tmp_node.next = current_head.next
                current_head = current_head.next
            index += 1
        return new_node.next 