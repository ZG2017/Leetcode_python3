# """
# # Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dummy = Node(0)
        cur_head = head
        pre_head = dummy
        holder = {}
        while cur_head:
            holder[cur_head] = Node(cur_head.val)
            pre_head.next = holder[cur_head]
            pre_head = holder[cur_head]
            cur_head = cur_head.next
        c = 0
        cur_head = head
        while cur_head:
            if cur_head.random:
                holder[cur_head].random = holder[cur_head.random]
            cur_head = cur_head.next
        return dummy.next
        
