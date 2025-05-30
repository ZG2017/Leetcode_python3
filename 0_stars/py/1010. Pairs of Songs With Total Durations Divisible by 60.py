class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0 
        holder = dict()
        for i in time:
            remain_time = i%60
            if 60-remain_time in holder:
                res += holder[60-remain_time]
            if remain_time == 0:
                remain_time = 60
            if remain_time not in holder:
                holder[remain_time] = 0
            holder[remain_time] += 1
        return res

