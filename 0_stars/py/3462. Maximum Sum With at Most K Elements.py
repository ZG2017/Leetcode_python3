# greedy + heap
class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        limits_holder = dict([(row_idx, limit) for row_idx, limit in enumerate(limits)])
        new_grid = []
        grid = [sorted(row) for row in grid]
        max_heap = [(-i[-1], row_idx) for row_idx, i in enumerate(grid)]
        heapq.heapify(max_heap)
        grid = [row[:-1] for row in grid]

        res = []

        while len(res) < k:
            cur_max = heapq.heappop(max_heap)
            cur_max_value, cur_max_row_idx = -cur_max[0], cur_max[1]
            if limits_holder[cur_max_row_idx] > 0:
                limits_holder[cur_max_row_idx] -= 1
                res.append(cur_max_value)
                if len(grid[cur_max_row_idx]) != 0:
                    heapq.heappush(max_heap, (-grid[cur_max_row_idx].pop(), cur_max_row_idx))
            else:
                continue
            # print(grid)
        return sum(res)
