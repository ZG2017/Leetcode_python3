# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = [(root, 1)]
        res = dict()
        while stack:
            tmp = stack.pop()
            if not tmp[0]:
                continue
            if tmp[1] not in res:
                res[tmp[1]] = []
            res[tmp[1]].append(tmp[0].val)
            if tmp[0].right:
                stack.append((tmp[0].right, tmp[1]+1)) 
            if tmp[0].left:
                stack.append((tmp[0].left, tmp[1]+1))
        holder = []
        print(res)
        for i in range(len(res), 0, -1):
            holder.append(res[i])
        return holder

                
