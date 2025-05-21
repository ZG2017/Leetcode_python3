# """
# # Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def helper(self, node):
        if not node.child and not node.next:
            self.cur_list += [node.val]
            return
        self.cur_list += [node.val]
        if node.child:
            self.helper(node.child)
        if node.next:
            self.helper(node.next)

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        self.cur_list = []
        self.helper(head)
        new_head = Node(self.cur_list[0])
        pre = new_head
        for i in self.cur_list[1:]:
            cur_node = Node(i)
            pre.next = cur_node
            cur_node.prev = pre
            pre = cur_node
        return new_head
            
        
