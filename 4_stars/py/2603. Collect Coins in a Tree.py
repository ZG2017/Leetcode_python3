# https://leetcode.com/problems/collect-coins-in-a-tree/solutions/3346183/python-code-with-human-readable-explanat-bjrp/

# idea:
# remove leaves untils all the leaves that don't have coins are removed.
# remove eaves by 2 layers.
# count the remaining edges (len(V)-1)
# multiply 2 because we need return to the start node.

class Solution(object):
    def collectTheCoins(self, coins, edges):
        """
        :type coins: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return 0

        n = len(edges) + 1

        g = {}
        for a, b in edges:
            for u, v in [(a, b), (b, a)]:
                if u in g:
                    g[u].add(v)
                else:
                    g[u] = set([v])

        leaves = [u for u in g if len(g[u])==1]
        for u in leaves:
            while len(g[u]) == 1 and coins[u] == 0:
                p = g[u].pop() 
                del g[u]
                g[p].remove(u)
                u = p


        for _ in range(2):
            leaves = [u for u in g if len(g[u])==1]
            for u in leaves:
                p = g[u].pop() 
                del g[u]
                g[p].remove(u)
                if len(g) < 2:
                    return 0
                

        return  2*(len(g)-1)