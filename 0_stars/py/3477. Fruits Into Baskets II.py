# since n < 100, we can just greedily place the fruits into the baskets with 2 for loops

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            placed = False
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced


# Or we can use segment tree to solve this problem if n is large
# detail explanation can be found for 3479. Fruits Into Baskets III

class Node():
    def __init__(self, node_list):
        self.list = node_list
        self.left = None
        self.right = None
        self.max = None

class max_segment_tree():
    def __init__(self, input_list):
        self.root = self.build(input_list)
    
    def build(self, cur_list):
        if len(cur_list) == 1:
            cur_node = Node(cur_list)
            cur_node.max = cur_list[0]
            return cur_node
        cur_node = Node(cur_list)
        left, right = cur_list[:len(cur_list)//2], cur_list[len(cur_list)//2:]
        cur_node.left = self.build(left)
        cur_node.right = self.build(right)
        cur_node.max = max(cur_node.left.max, cur_node.right.max)
        return cur_node
    
    def update(self, cur_node, input_fruit):
        if not cur_node:
            return None
        if len(cur_node.list) == 1: # leaf
            return None

        if cur_node.left and cur_node.left.max >= input_fruit:
            cur_node.left = self.update(cur_node.left, input_fruit)
        elif cur_node.right and cur_node.right.max >= input_fruit:
            cur_node.right = self.update(cur_node.right, input_fruit)

        # update cur_node
        if cur_node.left and cur_node.right:
            cur_node.max = max(cur_node.left.max, cur_node.right.max)
            cur_node.list = cur_node.left.list + cur_node.right.list
        elif cur_node.left:
            cur_node.max = cur_node.left.max
            cur_node.list = cur_node.left.list
        elif cur_node.right:
            cur_node.max = cur_node.right.max
            cur_node.list = cur_node.right.list
        else:
            cur_node = None
        return cur_node

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        segment_tree = max_segment_tree(baskets)
        # print(segment_tree.root.list, segment_tree.root.max)
        for fruit in fruits:
            if fruit <= segment_tree.root.max:
                segment_tree.root = segment_tree.update(segment_tree.root, fruit)
        return len(segment_tree.root.list) if segment_tree.root else 0


# or array implementation

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        N = 1
        while N <= n:
            N <<= 1
        
        segTree = [0] * (2 * N)
        
        for i in range(n):
            segTree[N + i] = baskets[i]
        
        for i in range(N - 1, 0, -1):
            segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])
        
        count = 0
        for fruit in fruits:
            index = 1
            if segTree[index] < fruit:
                count += 1
                continue
            
            while index < N:
                if segTree[2 * index] >= fruit:
                    index = 2 * index
                else:
                    index = 2 * index + 1
            
            segTree[index] = -1
            while index > 1:
                index //= 2
                segTree[index] = max(segTree[2 * index], segTree[2 * index + 1])
        
        return count