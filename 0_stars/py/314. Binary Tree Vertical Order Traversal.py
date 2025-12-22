# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs + deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        self.global_dict = dict()
        q = deque()
        q.append((root, 0))
        while len(q) != 0:
            cur_root, col_idx = q.popleft()
            if col_idx not in self.global_dict:
                self.global_dict[col_idx] = []
            self.global_dict[col_idx].append(cur_root.val)
            if cur_root.left:
                q.append((cur_root.left, col_idx-1))
            if cur_root.right:
                q.append((cur_root.right, col_idx+1))
        sorted_ans = [i[1] for i in sorted(self.global_dict.items(), key=lambda x: x[0])]
        return sorted_ans