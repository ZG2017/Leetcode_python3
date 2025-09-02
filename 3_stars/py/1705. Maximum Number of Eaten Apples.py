# greedy + heap

class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        import heapq
        d = 0
        holder = []
        ans = 0
        for i in range(len(apples)):
            cur_rot_days, cur_n_apples = days[i], apples[i]
            if cur_n_apples != 0:
                heapq.heappush(holder, (d + cur_rot_days, cur_n_apples))
            
            if len(holder) == 0:
                continue
            else:
                while holder: 
                    cur_rot_days, cur_n_apples = heapq.heappop(holder)
                    if cur_rot_days <= d:
                        continue
                    else:
                        ans += 1
                        cur_n_apples -= 1
                        if cur_n_apples != 0:
                            heapq.heappush(holder, (cur_rot_days, cur_n_apples))
                        break
            d += 1
            
        while holder:
            # print(holder)
            cur_rot_days, cur_n_apples = heapq.heappop(holder)
            if cur_rot_days <= d:
                continue
            else:
                ans += 1
                cur_n_apples -= 1
                if cur_n_apples != 0:
                    heapq.heappush(holder, (cur_rot_days, cur_n_apples))
                d += 1
        return ans