# find the start node and then use BFS to restore the array

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)


        for i in graph:
            if len(graph[i]) == 1:
                s = i
                break
        
        ans = [s]
        cur_node = s
        while len(ans) < len(graph):
            if len(graph[cur_node]) == 1:
                ans.append(graph[cur_node][0])
                cur_node = graph[cur_node][0]
            else:
                cand_node_1, cand_node_2 = graph[cur_node]
                if cand_node_1 == ans[-2]:
                    ans.append(cand_node_2)
                    cur_node = cand_node_2
                else:
                    ans.append(cand_node_1)
                    cur_node = cand_node_1
        return ans
