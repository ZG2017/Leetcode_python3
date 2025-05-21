# mine:（dp, TLE）
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if not primes:
            return 1
        saver = [0 for _ in range(len(primes))]
        sl = [1]
        c = 1
        while c < n:
            tmp_min = float("inf")
            for i in range(len(saver)):
                if primes[i]*sl[saver[i]] < tmp_min:
                    tmp_min = primes[i]*sl[saver[i]]
                    tmp_index = i
            saver[tmp_index] += 1
            if tmp_min == sl[-1]:
                continue
            sl.append(tmp_min)
            c += 1
        return sl[-1]



# mine:(heap, priority queue)
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        if not primes:
            return 1
        holder = [0 for _ in range(len(primes))]
        saver = primes.copy()
        h = primes.copy()
        heapq.heapify(h)
        sl = [1]
        c = 1
        while c < n:
            tmp = heapq.heappop(h)
            while h and tmp == h[0]:
                tmp = heapq.heappop(h)
            sl.append(tmp)
            while tmp in saver:
                tmp_index = saver.index(tmp)
                holder[tmp_index] += 1
                heapq.heappush(h,sl[holder[tmp_index]]*primes[tmp_index])
                saver[tmp_index] = sl[holder[tmp_index]]*primes[tmp_index]
            c += 1
        return sl[-1]

