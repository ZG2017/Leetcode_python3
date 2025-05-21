# updated:
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        total = 0
        mini = float("inf")
        tmp_index = 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < mini:
                mini = total
                tmp_index = i
        return tmp_index+1 if tmp_index+1 < len(gas) else 0
