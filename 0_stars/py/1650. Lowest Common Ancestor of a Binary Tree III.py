"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_parent = [p]
        while p.parent:
            p_parent.append(p.parent)
            p = p.parent
        
        q_parent = [q]
        while q.parent:
            q_parent.append(q.parent)
            q = q.parent
        
        overlap_set = set([n.val for n in p_parent]).intersection(set([n.val for n in q_parent]))
        # print(overlap_set)

        for i in p_parent:
            if i.val in overlap_set:
                return i
        return None


