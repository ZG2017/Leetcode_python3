# prefix tree

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_tree = dict()
        for integer in arr1:
            cur_tree = prefix_tree
            for char in str(integer):
                if char not in cur_tree:
                    cur_tree[char] = dict()
                cur_tree = cur_tree[char]
            cur_tree['END'] = True
        
        ans = 0
        for integer in arr2:
            cur_depth = 0
            cur_tree = prefix_tree
            for char in str(integer):
                if char not in cur_tree:
                    break
                else:
                    cur_depth += 1
                    cur_tree = cur_tree[char]
            ans = max(ans, cur_depth)
        return ans
