# dfs with queue

class Solution:
    def check_connection(self, node):
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if node not in self.visited:
                self.visited.add(node)
                for idx in range(len(self.isConnected)):
                    if self.isConnected[node][idx] == 1 and idx not in self.visited:
                        queue.append(idx)
        self.res += 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import deque
        self.isConnected = isConnected
        self.visited = set([])
        self.res = 0
        for i in range(len(isConnected)):
            if i in self.visited:
                continue
            self.check_connection(i)
        return self.res 