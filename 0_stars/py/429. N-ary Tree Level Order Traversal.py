# """
# # Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import OrderedDict
class Solution:
    def helper(self, node, level):
        if not node:
            return 
        if level not in self.holder:
            self.holder[level] = []
        self.holder[level].append(node.val)
        for i in node.children:
            self.helper(i, level+1)
        return

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.holder = OrderedDict()
        self.helper(root, 0)
        res = list(self.holder.values())
        return res




