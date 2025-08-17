# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# case by case
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        layer, is_full, is_complete = self.isFullComplete(root)
        # print(layer, is_full, is_complete)
        return is_complete
            
    def isFullComplete(self, root):
        if not root:
            return 0, True, True
        
        if not root.left and not root.right:
            return 1, True, True
        else:
            left_layer, is_left_full, is_left_complete = self.isFullComplete(root.left)
            right_layer, is_right_full, is_right_complete = self.isFullComplete(root.right)
            if left_layer - right_layer > 1 or left_layer - right_layer < 0:
                return max(left_layer, right_layer) + 1, False, False
            elif left_layer - right_layer == 1:
                if is_left_full:
                    return max(left_layer, right_layer) + 1, False, is_right_complete
                else:
                    return max(left_layer, right_layer) + 1, False, is_left_complete and is_right_full
            else:
                # left_layer - right_layer == 0
                if is_left_full:
                    if is_right_full:
                        return left_layer + 1, True, True
                    elif is_right_complete:
                        return left_layer + 1, False, True
                    else:
                        return left_layer + 1, False, False
                else:
                    return left_layer + 1, False, False
            
# deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        from collections import deque
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                break
            
        return not any(q)