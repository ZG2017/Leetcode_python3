# recursive


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def smallest(self, s1, s2):
        if s1 == '':
            return s2
        smaller_s = s1 if len(s1) < len(s2) else s2
        smaller_len = min(len(s1), len(s2))
        if s1[:smaller_len+1] < s2[:smaller_len+1]:
            return s1
        elif s1[:smaller_len+1] == s2[:smaller_len+1]:
            return smaller_s
        else:
            return s2
    
    def walk(self, cur_s, cur_root):
        if cur_root.left:
            self.walk(cur_s+chr(cur_root.val+97), cur_root.left)
        if cur_root.right:
            self.walk(cur_s+chr(cur_root.val+97), cur_root.right)
        if not cur_root.left and not cur_root.right:
            cur_s += chr(cur_root.val+97)
            self.smallest_s = self.smallest(self.smallest_s, cur_s[::-1])
        return

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smallest_s = ''
        self.walk('', root)
        return self.smallest_s



