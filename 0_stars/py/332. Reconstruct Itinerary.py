# mine: DSF
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import bisect
        dit = {}
        for i in tickets:
            if i[0] not in dit:
                dit[i[0]] = []
            if i[1] not in dit:
                dit[i[1]] = []
            bisect.insort(dit[i[0]],i[1])
        target = len(tickets)+1
        res = ["JFK"]
        def helper(lens):
            if lens == target:
                return True
            for i in range(len(dit[res[-1]])):
                tmp = dit[res[-1]].pop(i)
                res.append(tmp)
                flag = helper(lens+1)
                if flag:
                    return True
                res.pop()
                dit[res[-1]].insert(i,tmp)
        helper(1)
        return res

