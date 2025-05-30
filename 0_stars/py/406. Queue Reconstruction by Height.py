class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        holder = dict()
        for height, pre in people:
            if height not in holder:
                holder[height] = []
            holder[height].append([height, pre])
        for i in holder:
            holder[i] = sorted(holder[i], key = lambda x:x[1])
        res = []
        for i in sorted(list(holder.keys()), reverse = True):
            for p in holder[i]:
                res.insert(p[1], p)
        return res
        
