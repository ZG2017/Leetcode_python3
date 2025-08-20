# first, find communities by union find
# second, find adj and BFS to get invoked nodes
# third, find remaining nodes

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque
        
        self.tree = dict()
        self.groups = dict()
        self.adj = dict([(i, []) for i in range(n)])
        self.k = k
        self.n = n
        
        # find communities
        self.find_communities(invocations)
        
        # find adj
        for src, tar in invocations:
            self.adj[src].append(tar)
        
        # find invoked nodes
        invoked_nodes = self.get_invoked()
        
        # find remaining nodes
        remains = []
        for group_idx_list in self.groups.values():
            if len(group_idx_list) != len(invoked_nodes):
                remains.extend(group_idx_list)
            else:
                if set(group_idx_list) == invoked_nodes:
                    continue
                else:
                    remains.extend(group_idx_list)
        return sorted(remains)

    def get_invoked(self):
        ans = []
        visited = [False] * self.n
        if self.k not in self.adj:
            return ans
        else:
            dq = deque([self.k])
            while dq:
                cur_node = dq.popleft()
                ans.append(cur_node)
                visited[cur_node] = True
                if cur_node not in self.adj:
                    continue
                for i in self.adj[cur_node]:
                    if not visited[i]:
                        visited[i] = True
                        dq.append(i)
                        ans.append(i)
            return set(ans)

    def get_root(self, node, c):
        if node not in self.tree:
            self.tree[node] = node
            return c, node
        else:
            if node == self.tree[node]:
                return c + 1, node
            else:
                return self.get_root(self.tree[node], c + 1)

    def find_communities(self, invocations):
        # union find
        for src, tar in invocations:
            src_c, src_root = self.get_root(src, 0)
            tar_c, tar_root = self.get_root(tar, 0)
            if src_root != tar_root:
                if src_c >= tar_c:
                    self.tree[tar_root] = src_root
                else:
                    self.tree[src_root] = tar_root
        # get communities based on tree
        for i in range(0, self.n):
            _, cur_root = self.get_root(i, 0)
            if cur_root not in self.groups:
                self.groups[cur_root] = []
            self.groups[cur_root].append(i)
                

        
        