# heapq sort and hashmap

class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq
        c = Counter(s)
        holder = [(-v, char)  for char, v in c.items()]
        heapq.heapify(holder)
        cur_res = ''
        tmp = None
        while holder:
            c, char = heapq.heappop(holder)
            if cur_res and char == cur_res[-1] and len(holder) == 0:
                return ''
            elif cur_res and char == cur_res[-1] and len(holder) != 0:
                tmp = (c, char)
                c, char = heapq.heappop(holder)
                cur_res += char
                c += 1
                if c != 0:
                    heapq.heappush(holder, (c, char))
                heapq.heappush(holder, tmp)
            else:
                cur_res += char
                c += 1
                if c != 0:
                    heapq.heappush(holder, (c, char))
        return cur_res

