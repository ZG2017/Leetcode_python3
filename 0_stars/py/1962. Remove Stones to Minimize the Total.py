# heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        piles = [-i for i in piles]
        heapq.heapify(piles)

        for i in range(k):
            cur_reduced = heapq.heappop(piles)//2
            if cur_reduced == 0:
                break
            heapq.heappush(piles, cur_reduced)
        return sum([-i for i in piles])

