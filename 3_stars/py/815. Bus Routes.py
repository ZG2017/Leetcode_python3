# OOM
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        from collections import deque, defaultdict
        adj_dict = defaultdict(set)
        for idx, i in enumerate(routes):
            for j in range(len(i)-1):
                for k in range(j+1, len(i)):
                    adj_dict[i[j]].add(i[k])
                    adj_dict[i[k]].add(i[j])
        
        dq = deque()

        visited = set([])
        found_flag = False

        dq.append(source)
        prev_stop = defaultdict()

        while dq and not found_flag:
            cur_stop = dq.popleft()
            for i in adj_dict[cur_stop]:

                if i not in visited:
                    visited.add(i)
                    dq.append(i)
                    prev_stop[i] = cur_stop
                    if i == target:
                        found_flag = True
                        break
        
        if not found_flag:
            return -1
        res = 0
        cur_stop = target
        while cur_stop != source:
            cur_stop = prev_stop[cur_stop]
            res += 1
        return res


# refer: https://leetcode.com/problems/bus-routes/solutions/1072394/python-bfs-solution/
# don't need to create adjacent list, just need to store the buses going to a stop

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if target == source:
            return 0

        from collections import deque, defaultdict
        adj_dict = defaultdict(set)
        for idx, i in enumerate(routes):
            for j in i:
                adj_dict[j].add(idx)
        
        dq = deque()

        visited_stops = set([])
        visited_routes = set([])
        found_flag = False

        dq.append(source)
        prev_stop = defaultdict()

        while dq and not found_flag:
            cur_stop = dq.popleft()
            for j in adj_dict[cur_stop]:
                if j not in visited_routes:
                    visited_routes.add(j)
                    for i in routes[j]:
                        if i not in visited_stops:
                            visited_stops.add(i)
                            dq.append(i)
                            prev_stop[i] = cur_stop
                            if i == target:
                                found_flag = True
                                break
        
        if not found_flag:
            return -1
        res = 0
        cur_stop = target
        while cur_stop != source:
            cur_stop = prev_stop[cur_stop]
            res += 1
        return res
                


        
