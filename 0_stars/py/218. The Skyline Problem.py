# mine:(TLE)
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        stack = [(buildings[0][0],0)]
        holder = []
        saver = {}
        res = []
        for i in buildings:
            holder.append([i[0],i[2]])
            holder.append([i[1],i[2]])
            saver[(i[0],i[2])] = (i[1],i[2])
        holder = sorted(holder, key = lambda i:i[0])
        for i in range(len(holder)):
            tui = tuple(holder[i])
            if tui == stack[-1]:
                tmp = stack.pop()
                if tmp[1] > stack[-1][1]:
                    if i == len(holder)-1 or holder[i+1][0] != tmp[0]:
                        res.append([tmp[0],stack[-1][1]])
            elif tui in stack:
                while tui in stack:
                    stack.remove(tui)
            elif holder[i][1] > stack[-1][1]:
                if res and holder[i][0] == res[-1][0]:
                    res.pop()
                if not res or holder[i][1] != res[-1][1]:
                    res.append(holder[i])
                stack.append(saver[tui])
            elif holder[i][1] == stack[-1][1]:
                stack.append(saver[tui])
            else: 
                index = len(stack)-2
                while holder[i][1] < stack[index][1]:
                    index -= 1
                if holder[i][1] == stack[index][1]:
                    if saver[tui][0] > stack[index][0]:
                        stack = stack[:index]+[saver[tui]]+stack[index:]
                    else:
                        stack = stack[:index+1]+[saver[tui]]+stack[index+1:]
                else:
                    stack = stack[:index+1]+[saver[tui]]+stack[index+1:]
        return res
