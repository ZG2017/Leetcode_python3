# dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_res = 0

        def helper(root):
            if not root.left and not root.right:
                return root.val, root.val
            
            left_max, left_min, left_candidate_1, left_candidate_2 = None, None, None, None
            if root.left:
                left_max, left_min = helper(root.left)
                left_candidate_1 = abs(root.val - left_max)
                left_candidate_2 = abs(root.val - left_min)
            
            right_max, right_min, right_candidate_1, right_candidate_2 = None, None, None, None
            if root.right:
                right_max, right_min = helper(root.right)
                right_candidate_1 = abs(root.val - right_max)
                right_candidate_2 = abs(root.val - right_min)

            res_holder = [i for i in [self.max_res, left_candidate_1, left_candidate_2, right_candidate_1, right_candidate_2] if i != None]

            self.max_res = max(res_holder)

            max_holder = [i for i in [left_max, right_max, root.val] if i != None]
            cur_max = max(max_holder)

            min_holder = [i for i in [left_min, right_min, root.val] if i != None]
            cur_min = min(min_holder)

            return cur_max, cur_min
            
        helper(root)
        return self.max_res


# better dfs
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/solutions/7273425/simple-python-solution-beats-100-by-user-0geq/

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mn, mx):
            if not node:
                return mx - mn
            mn = min(mn,node.val)
            mx = max(mx,node.val)
            return max(dfs(node.left, mn, mx), dfs(node.right, mn, mx))
        return dfs(root, root.val, root.val)