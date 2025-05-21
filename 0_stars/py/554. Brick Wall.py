# Memory Limit Exceeded

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        row_sum = sum(wall[0])
        holder = dict([(i, len(wall)) for i in range(row_sum)])
        for row in wall:
            cur_sum = 0
            for brick in row[:-1]:
                cur_sum += brick
                holder[cur_sum] -= 1
        return min(holder.values())


# dont need to remember all the gaps:

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        holder = dict()

        for row in wall:
            cur_sum = 0
            for brick in row[:-1]:
                cur_sum += brick
                if cur_sum not in holder:
                    holder[cur_sum] = 0
                holder[cur_sum] += 1
        if len(holder.values()) == 0:
            return len(wall)
        return len(wall) - max(holder.values())
