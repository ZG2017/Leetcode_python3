# sorted events and count the maximum number of concurrent events
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        ans = cur = 0
        print(events)
        for _, e in events:
            cur += e
            ans = max(ans, cur)
        return ans


# priority queue version

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        q = []
        for interval in intervals:
            start, end = interval
            q.append((start, 1))
            q.append((end, 0))
        heapq.heapify(q)
        c = 0
        max_c = 0
        while q:
            cur = heapq.heappop(q)
            if cur[1] == 1:
                c += 1
                max_c = max(c, max_c)
            else:
                c -= 1
        return max_c

