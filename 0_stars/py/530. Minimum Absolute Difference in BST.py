# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        st = []
        p = root
        pre = -float('inf')
        min_val = float('inf')
        while p or st:
            while p:
                st.append(p)
                p = p.left
            p = st.pop()
            cur = p.val
            if cur - pre < min_val:
                min_val = cur - pre
            pre = cur
            p = p.right
        return min_val
